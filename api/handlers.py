#!/usr/bin/python
# -*- coding: utf-8 -*-

from piston.handler import BaseHandler
from ibge_portal.ibge_cidades.models import Estado, Cidade

class EstadoHandler (BaseHandler):
	allowed_methods = ('GET',)
	model = Estado

	def read(self, request):
		estados = Estado.objects.all()
		return estados

class CidadeHandler(BaseHandler):
	allowed_methods = ('GET',)
	model = Cidade


	def read(self, request, sigla_estado):
		print 'ok'
		print sigla_estado
		cidades = Cidade.objects.filter(estado__sigla = sigla_estado)
		return cidades		