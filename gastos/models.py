from django.db import models

class Gasto(models.Model):
	dia = models.DateField()
	valor = models.DecimalField(max_digits=4,decimal_places=2)
	quantidade = models.IntegerField()

	def __unicode__(self):
		return str(self.dia)

class Pessoa(models.Model):
	nome = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nome


class GastosPessoa(models.Model):
	gasto = models.ForeignKey(Gasto)
	pessoa = models.ForeignKey(Pessoa)
	quantidade = models.IntegerField()