from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.forms.models import inlineformset_factory
from models import *

def home(request):

	creditos = Pessoa.objects.all()
	#gastos = GastosPessoa.objects.filter(pago=False).order_by('pessoa')

	VARS = { 
		#'gastos': gastos,
	   	'creditos': creditos,
	}
	
	return render_to_response('home.html', VARS, context_instance=RequestContext(request))