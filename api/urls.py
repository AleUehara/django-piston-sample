#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from piston.resource import Resource
from ibge_portal.api.handlers import EstadoHandler, CidadeHandler

estado_resource = Resource(EstadoHandler)
cidade_resource = Resource(CidadeHandler)

urlpatterns = patterns( '',
	(r'^estados/', estado_resource),
	(r'^cidades/(?P<sigla_estado>[^/]+)', cidade_resource),
)