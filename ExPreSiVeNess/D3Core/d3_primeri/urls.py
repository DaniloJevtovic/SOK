from d3_primeri import prodavnica_view
from django.conf.urls import url

from . import views, expness_views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ucitavanje/plugin/(?P<id>([a-z]+|[_])+)$', views.ucitavanje_plugin, name="ucitavanje_plugin"),
    url(r'^prikazivanje/plugin/(?P<id>([a-z]+|[_])+)$', views.prikazivanje_plugin, name="prikazivanje_plugin"),

    url(r'^primer1$', views.primer1, name="primer1"),
    url(r'^primer2$', views.primer2, name="primer2"),
    url(r'^primer3$', views.primer3, name="primer3"),
    url(r'^primer4$', views.primer4, name="primer4"),


    url(r'^primer/pan/zoom$', views.primerPanZoom, name="primerPanZoom"),
    url(r'^sok/$', views.sok_view , name="sok_view"),
    url(r'^test/$', expness_views.test_view, name="test"),
    url(r'^main/$', expness_views.main_view, name="main_view"),
    url(r'^show/$', expness_views.show_view, name="show_view"),
]