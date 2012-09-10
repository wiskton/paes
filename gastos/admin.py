# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms

from models import *

class PessoaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'credito',)
	save_on_top = True
	list_filter = ('nome',)
	
class GastosPessoAdmin(admin.ModelAdmin):
	list_display = ('gasto', 'pessoa', 'quantidade', 'valor', 'pago' )
	save_on_top = True
	list_filter = ('gasto', 'pessoa','pago')
		
class GastosPessoaInline( admin.TabularInline ):
	model = GastosPessoa
	extra = 4

class GastosAdmin(admin.ModelAdmin):
	list_display = ('dia', 'valor', 'quantidade',)
	save_on_top = True
	list_filter = ('dia',)
	date_hierarchy = 'dia'

	inlines = [ GastosPessoaInline, ]

admin.site.register(Gasto, GastosAdmin)
admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(GastosPessoa, GastosPessoAdmin)
