from django.contrib import admin

from .models import peliculas,usuario,Alquiler
# Register your models here.

@admin.register(peliculas)
class  pelisAdmin(admin.ModelAdmin):
	list_display = ('titulo','imagen','genero', 'precio', 'director', 'pais',)
     
#admin.site.register(peliculas, pelisAdmin)
	

@admin.register(usuario)
class  usuarioAdmin(admin.ModelAdmin):
	pass
#admin.site.register(usuario, usuarioAdmin)

@admin.register(Alquiler)
class Alquileradmin(admin.ModelAdmin):
	list_display = ('cliente','cantidad_pelicula','Pelicula','precio')

