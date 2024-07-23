from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Edificio

# Agregar la clase Estudiante para administrar desde
# interfaz de administración
# admin.site.register(Estudiante)

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Estudiante
class EdificioAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'direccion', 'ciudad','tipo')

# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin
admin.site.register(Edificio, EdificioAdmin)