# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from models import *

class GastosPessoaInline( admin.TabularInline ):
	model = GastosPessoa
	extra = 3

class GastosAdmin(admin.ModelAdmin):
	list_display = ('dia', 'valor', 'quantidade',)
	save_on_top = True
	list_filter = ('dia',)
	date_hierarchy = 'dia'

	inlines = [ GastosPessoaInline, ]

admin.site.register(Gasto, GastosAdmin)
admin.site.register(Pessoa)
