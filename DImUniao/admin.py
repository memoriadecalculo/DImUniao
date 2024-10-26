#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.contrib.admin import site
from import_export.admin import ImportExportModelAdmin
from DImUniao import models, resources

class Depreciacao(ImportExportModelAdmin):
    resource_class = resources.Depreciacao
    list_display = ('IDX', 'REF', 'MES', 'UGE', 'RIPU', 'DATA_AVALIA', 'VBENFEITORIA', 'VDEPRECMES', 'VDEPRECACUMU', 'CC')
    search_fields = ('REF', 'UGE', 'RIPU', 'DATA_AVALIA', 'CC')
    #fields = ('antiguidade', 'sigla', 'descricao',)
    readonly_fields = []
    list_editable = []
    ordering = ('RIPU',)
    list_filter = ['REF', 'UGE', 'CC', 'RIPU']
    filter_horizontal = []

site.register(models.Depreciacao, Depreciacao)
