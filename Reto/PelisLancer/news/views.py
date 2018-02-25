from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView, CreateView
from django.views.generic.list import ListView
from .models import peliculas, Alquiler,Login
# Create your views here.

#class IndexListView(ListView):
#			model = peliculas

class index(TemplateView):
	template_name = 'index.html'
	#return render_to_response('news.index.html')

	"""class IndexNew(TemplateView):
		template_name = 'index.html'

		def get_context_data(self, username='ts',**kwards):
			context = super(IndexNew, self).get_context_data(**kwards)

	response = {}
	response['username'] = username

	context.update(response)
	return context """
	

class IndexListView(ListView):
	model = peliculas
		



class AlquilerPelis(ListView):
	model =  Alquiler
	template_name = 'alquiler.html'
	def peliculasLis(request):
		pelis = peliculas.object.all()
		contexto = {'peliculas': pelis}
		return render(request,'alquiler.html',contexto)

		

class login(ListView):
	model = Login
	template_name = 'login_list.html'


	
