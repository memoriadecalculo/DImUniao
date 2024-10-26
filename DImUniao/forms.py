#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from    django.forms                import Form
from    django.forms.fields         import CharField

class home(Form):
    """Define o RIP Utilização"""
    
    RIPU = CharField(label='RIP Utilização')
    
    class Meta:
        fields = '__all__'
