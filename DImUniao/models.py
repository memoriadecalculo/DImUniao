#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db.models import Model, CharField, DateField, DecimalField, PositiveSmallIntegerField

class Depreciacao(Model):
    REF          = CharField(max_length=200)
    UGE          = CharField(max_length=200)
    RIPU         = CharField(max_length=200)
    DATA_AVALIA  = DateField(null=True, blank=True, verbose_name='data da última avaliação')#CharField(max_length=200, verbose_name="Data da última avaliação")
    VBENFEITORIA = DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Valor da Benfeitoria')
    VDEPRECMES   = DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Valor de depreciação no mês(R$)')
    VDEPRECACUMU = DecimalField(max_digits=20, decimal_places=2, null=True, blank=True, verbose_name='Valor acumulado de depreciação desde a ultima avaliação(R$)')
    CC           = CharField(max_length=200, null=True)
    MES          = DateField(null=True, blank=True, verbose_name='mês')
    
    def __str__(self):
        return self.REF + self.RIPU
  
    def filename(self):
        return self.REF + self.RIPU

    class Meta:
        unique_together = (('REF', 'RIPU'),)
        ordering = ['RIPU', 'REF',]
    
    def IDX(self):
        return self.RIPU + '-' + self.REF