#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from import_export.resources import ModelResource
from DImUniao import models

class Depreciacao(ModelResource):
    class Meta:
        model = models.Depreciacao

