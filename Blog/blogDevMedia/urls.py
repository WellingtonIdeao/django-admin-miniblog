from django.conf.urls import url
from . views import *

urlpatterns = [
    url(r'^listar/', postagem, name='home'),
    url(r'^post/(?P<pk>[0-9]+)', postagem_list, name='post'),
]
