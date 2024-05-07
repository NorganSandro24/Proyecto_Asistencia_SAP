from django.contrib import admin
# Importa el módulo de administración de Django
from .models import Task
# Importa el modelo Task desde el archivo models.py de la misma aplicación
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
    # Define una clase TaskAdmin que hereda de admin.ModelAdmin y configura el campo 
    # 'created' como de solo lectura en el panel de administración

admin.site.register(Task, TaskAdmin)
# Registra el modelo Task en el panel de administración de 
# Django utilizando la clase TaskAdmin para personalizar su visualización y comportamiento en el panel