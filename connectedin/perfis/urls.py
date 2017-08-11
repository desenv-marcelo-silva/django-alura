from django.conf.urls import patterns, url
from perfis.views import index, exibir

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', exibir, name='exibir')
)