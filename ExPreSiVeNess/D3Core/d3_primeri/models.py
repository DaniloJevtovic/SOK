from django.db import models

class Prodavnica(models.Model):
    pib=models.CharField(max_length=20)
    naziv=models.CharField(max_length=50)
    adresa=models.CharField(max_length=40)
    broj_telefona=models.CharField('broj telefona',max_length=30)


    def __str__(self):
        return self.naziv

class Kategorija(models.Model):
    oznaka=models.CharField(max_length=20)
    naziv=models.CharField(max_length=50)

    def __str__(self):
        return self.naziv


class Artikal(models.Model):
    oznaka=models.CharField(max_length=20)
    naziv=models.CharField(max_length=50)
    opis=models.TextField(max_length=200)
    cena=models.DecimalField(max_digits=8,decimal_places=2)
    na_akciji=models.BooleanField('na akciji')
    kategorije=models.ManyToManyField(Kategorija)
    prodavnica=models.ForeignKey(Prodavnica,on_delete=models.CASCADE,related_name='artikli')

    def __str__(self):
        return self.naziv

class Element(models.Model):
    name=models.CharField(max_length=50)
    text=models.CharField(max_length=200, null=True)
    def __str__(self):
        return "Element [ " + self.name + " ]"

class Attribute(models.Model):
    name=models.CharField(max_length=50)
    value=models.CharField(max_length=100)
    parent=models.ForeignKey(Element, on_delete=models.CASCADE, related_name='attribs')

    def __str__(self):
        return "Attribute [ name = " + self.name + ", value = " + self.value + " ]"

class Link(models.Model):
    name = models.CharField(max_length=50)
    source = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='from_links')
    target = models.ForeignKey(Element, on_delete=models.CASCADE, related_name='to_links')

    def __str__(self):
        return "Link [ " + self.source + ", " + self.target + " ]"