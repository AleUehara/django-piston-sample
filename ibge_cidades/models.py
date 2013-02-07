#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Estado(models.Model):
  sigla = models.CharField(max_length = 2)
  nome = models.CharField(max_length = 100)

class Cidade(models.Model):
  nome = models.CharField(max_length = 100)
  estado = models.ForeignKey('Estado')
