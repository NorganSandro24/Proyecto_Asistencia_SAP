from django.apps import AppConfig
# Importa la clase base AppConfig del módulo django.apps

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Define el campo predeterminado para la clave primaria como BigAutoField
    name = 'tasks'
    # Especifica el nombre de la aplicación, en este caso, 'tasks'
