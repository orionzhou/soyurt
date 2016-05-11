from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^strains$', views.strains, name = 'strains'),
    url(r'^locations$', views.locations, name = 'locations'),
    url(r'^phenotypes$', views.phenotypes, name = 'phenotypes'),
    url(r'^tests$', views.tests, name = 'tests'),
    url(r'^observations$', views.observations, name = 'observations'),
]
