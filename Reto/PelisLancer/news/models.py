from django.db import models
from django.utils.html import format_html
from django.shortcuts import render

# Create your models here.


class peliculas(models.Model):
	id = models.IntegerField( primary_key=True,blank=True)
	titulo = models.CharField(max_length=70)
	genero = models.CharField(max_length=70)
	imagen = models.ImageField(upload_to='pelis-image',null=True)
	#Cliente = models.ForeignKey("usuario", on_delete=models.CASCADE, null = True)
	precio = models.FloatField(null=True)
	Sinópsis = models.TextField(null=True)
	director = models.CharField(max_length=70,null = False)
	pais = models.CharField(max_length=70,null = False)


 
def image_tag (self):
    	return format_html(" <image src='{}' />".format(self.image.url))
    	image_tag.allow_tags = True






class usuario(models.Model):
   nombre = models.CharField(max_length=70) 
   apellido = models.CharField(max_length=70)
   foto = models.ImageField(upload_to='usuario-image',null = True)
   #create_at = models.DateTimeField(auto_now=False, auto_now_add=False,null = True)
   #update_at = models.DateTimeField(auto_now=False, auto_now_add=False,null = True)
   Correo = models.EmailField( null=True)
   TarjetaCredito = models.CharField(max_length=19, null = True)
 
   def __str__ (self):
    return "%s %s" % (self.nombre, self.apellido)



	


class Alquiler(models.Model):
	cliente = models.ForeignKey(usuario, null = True, blank = True,on_delete=models.CASCADE)
	cantidad_pelicula = models.IntegerField(null=True)
	Pelicula = models.ForeignKey(peliculas, null=True, blank=True, on_delete=models.CASCADE)	
	fecha_Alquier =  models.CharField(max_length=10 ,null = True)
	fechaDevolucion =  models.CharField(max_length=10 ,null = True)
	Comprobante_devolucion = models.CharField(max_length=10 ,null = True)
	precio = models.FloatField(null=True)
#cobraMora =  models.ForeignKey("CobraMora", null=True, blank=True, on_delete=models.CASCADE)
#	mora = CobraMora(precio)
	
def CobraMora(precio,fechaDevolucion,Comprobante_devolucion):
	if str(fechaDevolucion) > str(Comprobante_devolucion):
	 precio = str(float(precio * 0.05))
	 return precio

class Login(models.Model):
	Usuario = models.CharField(max_length=70)
	password = models.CharField(max_length=15)