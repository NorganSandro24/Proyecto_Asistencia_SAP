from django.forms import ModelForm
# Importa la clase ModelForm del módulo django.forms

from .models import Task
# Importa el modelo Task desde el archivo models.py de la misma aplicación

class TaskForm(ModelForm):
    # Define una clase TaskForm que hereda de ModelForm para crear un formulario basado en un modelo
    class Meta:
        model = Task
        # Especifica que este formulario se basa en el modelo Task
        fields = ['title', 'description', 'important']
        # Define los campos del formulario que se utilizarán, en este caso, 
        # 'title', 'description' y 'important' del modelo Task