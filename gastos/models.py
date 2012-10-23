from django.db import models

class Gasto(models.Model):
	dia = models.DateField()
	valor = models.DecimalField(max_digits=4,decimal_places=2)
	quantidade = models.IntegerField()

	class Meta:
		ordering = ['dia']

	def __unicode__(self):
		return str(self.dia)

class Pessoa(models.Model):
	nome = models.CharField(max_length=255)
	credito = models.DecimalField(max_digits=4,decimal_places=2)

	def total_pago(self):
		gastos = GastosPessoa.objects.filter(pessoa=self,pago=False)
		total = 0
		for i in gastos:

			quantidade = i.quantidade
			total_quantidade = i.gasto.quantidade
			total_valor = i.gasto.valor
			valor = (quantidade * (total_valor/total_quantidade))

			total += valor

		return '%.2f' % total

	def falta_pagar(self):
		pessoa = self
		gastos = GastosPessoa.objects.filter(pessoa=pessoa,pago=False)
		total = 0
		for i in gastos:

			quantidade = i.quantidade
			total_quantidade = i.gasto.quantidade
			total_valor = i.gasto.valor
			valor = (quantidade * (total_valor/total_quantidade))

			total += valor

		total = total - self.credito
		return '%.2f' % total

	def __unicode__(self):
		return self.nome


class GastosPessoa(models.Model):
	gasto = models.ForeignKey(Gasto)
	pessoa = models.ForeignKey(Pessoa)
	quantidade = models.IntegerField()
	pago = models.BooleanField(default=False)
	
	def valor(self):
		quantidade = self.quantidade
		total_quantidade = self.gasto.quantidade
		total_valor = self.gasto.valor
		valor = (quantidade * (total_valor/total_quantidade))
		return '%.2f' % valor
	valor.is_safe = True
	valor.allow_tags = True
	valor.short_description = u'Valor'