from django.template import Template, RequestContext
from django.http import HttpResponse
from django.shortcuts import render
from django.apps.registry import apps
from django.shortcuts import redirect

from .models import Element, Attribute, Link
from .tree import TreeNode

def test_view(request):
    template = Template('''
    {% extends "base.html" %}
    {% block content %}
        {% for neko in neki %}
        {{ neko }}<br/>
        {% endfor %}
    {% endblock content %}
    
    ''')
    context = RequestContext(request, {
        "neki" : [ "X", "Y", "Z" ]
    })
    print(request.POST['plugin_za_ucitavanje'])
    print(request.POST['plugin_za_prikaz'])
    return HttpResponse(template.render(context))

def main_view(request):
    app_config = apps.get_app_config('d3_primeri')
    context = {
        "plugini_za_ucitavanje" : app_config.plugini_ucitavanje,
        "plugini_za_prikaz" : app_config.plugini_prikaz,
    }
    return render(request, 'ExPreSiVeNessBase.html', context)

def show_view(request):
    app_config = apps.get_app_config('d3_primeri')

    plugin_za_ucitavanje_id = request.POST['plugin_za_ucitavanje']
    plugin_za_prikaz_id = request.POST['plugin_za_prikaz']

    izabrani_plugin_ucitavanje = None
    izabrani_plugin_prikaz = None

    for plugin_u in app_config.plugini_ucitavanje:
        if plugin_u.identifier() == plugin_za_ucitavanje_id:
            izabrani_plugin_ucitavanje = plugin_u
            break

    for plugin_p in app_config.plugini_prikaz:
        if plugin_p.identifier() == plugin_za_prikaz_id:
            izabrani_plugin_prikaz = plugin_p
            break

    izabrani_plugin_ucitavanje.ucitati()

    links = Link.objects.all()
    elements = Element.objects.all()

    root = create_tree(elements, links)

    treeJson = printTreeJson(root)
    # Debug
    print(treeJson)
    # Debug

    if plugin_za_prikaz_id != "prikazati_jednostavno_graf":
        template = Template(izabrani_plugin_prikaz.prikazati())
        context = RequestContext(request, {
            "plugini_za_ucitavanje": app_config.plugini_ucitavanje,
            "plugini_za_prikaz": app_config.plugini_prikaz,
            "plugin_uc": izabrani_plugin_ucitavanje,
            "plugin_pr": izabrani_plugin_prikaz,
            "elementi": elements,
            "linkovi": links,
            "drvo" : treeJson
        })
        return HttpResponse(template.render(context))
    else:
        return izabrani_plugin_prikaz.prikazati(request)

def create_tree(elements, links):
    # Debug
    print("Postoji " + str(len(elements)) + " elemenata")
    print("Postoji " + str(len(links)) + " veza")
    # Debug

    uninserted_elements = {}
    linked_elements = {}
    roots = {}
    top_root = None

    for element in elements:
        uninserted_elements[element.id] = element

    # Debug
    print("U rijecniku postoji " + str(len(uninserted_elements)) + " elemenata")
    # Debug

    for link in links:
        if link.source.id in linked_elements:
            linked_elements[link.source.id].append(link.target)
        else:
            linked_elements[link.source.id] = [ link.target ]

    # Debug
    ukupno = 0
    for k, v in linked_elements.items():
        print("Element " + uninserted_elements[k].name + " ima " + str(len(v)) + " veza")
        ukupno = ukupno + len(v)

    print("To je ukupno " + str(ukupno) + " veza")
    # Debug

    while len(uninserted_elements) != 0:
        root_candidate = uninserted_elements.pop(next(iter(uninserted_elements)))
        # Debug
        print("Korijen hijerarhije: <" + root_candidate.name + ">" + getString(root_candidate.text))
        # Debug
        top_root = form_hierarchy(None, root_candidate, uninserted_elements, roots, linked_elements)

    if len(roots) > 1:
        top_root = TreeNode(None)
        for k, v in roots.items():
            top_root.children.append(v)

    return top_root

def form_hierarchy(parent, element, uninserted_elements, roots, linked_elements):
    node = TreeNode(element)
    # Debug
    print("Formiran cvor <" + element.name + "> - id : " + str(element.id))
    # Debug
    if parent != None:
        node.parent = parent
        # Debug
        print("Roditeljski cvor <" + node.parent.object.name + "> - id : " + str(node.parent.object.id))
        # Debug
        node.parent.children.append(node)
        # Debug
        print("Roditelj : " + str(node.parent) )
        print("Djeca {")
        for nd in node.parent.children:
            print("Cvor <" + nd.object.name + "> - id : " + str(nd.object.id))
        print("}")
        # Debug
        if element.id in roots:
            del roots[id]
    else:
        roots[element.id] = node

    try:
        del uninserted_elements[element.id]
        print('broj neumetnutih elemenata ' + str(len(uninserted_elements)))
    except KeyError:
        # Debug
        print('Greska kod brisanja id ' + str(element.id))
        # Debug

    if element.id in linked_elements:
        for linked_element in linked_elements[element.id]:
            if linked_element.id in uninserted_elements or linked_element.id in roots:
                form_hierarchy(node, linked_element, uninserted_elements, roots, linked_elements)

    return node

def getString(str):
    if str is None:
        return ''
    return str

def printTreeJson(node):
    myContent = "{" # Pocetak
    elm = node.object
    if elm is not None:
        myContent += '"name":'+ '"element_' + str(elm.id) + '",'
        myContent += '"naziv":' + '"' + getString(elm.name) + '",'
        myContent += '"tekst":' + '"' + getString(elm.text) + '",'
        myContent += '"atributi":['
        for attr in elm.attribs.all():
            myContent += '{"roditelj":' + '"element_' + str(attr.parent.id) + '",'
            myContent += '"naziv":' + '"' + getString(attr.name) + '",'
            myContent += '"vrijednost":' + '"' + getString(attr.value) + '"},'
        if len(elm.attribs.all()) > 0:
            myContent = myContent[:-1]
        myContent += "],"
    else:
        myContent += '"name":' + '"root",'
        myContent += '"naziv":' + '"Root",'
    myContent += '"children":['
    childrenContent = ""
    for child in node.children:
        childrenContent += printTreeJson(child)
        childrenContent += ","
    childrenContent = childrenContent[:-1] + "]"

    return myContent + childrenContent + "}"  # Kraj
