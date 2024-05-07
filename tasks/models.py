from django.db import models
from django.contrib.auth.models import User
# Importa el modelo User de django.contrib.auth.models para relacionar cada tarea con un usuario

class Task(models.Model):
    title = models.CharField(max_length=200)
    # Un campo de texto corto para el título de la tarea
    description = models.TextField(max_length=1000)
    # Un campo de texto largo para la descripción de la tarea
    created = models.DateTimeField(auto_now_add=True)
    # Un campo de fecha y hora que se establece automáticamente cuando se crea la tarea
    datecompleted = models.DateTimeField(null=True, blank=True)
    # Un campo de fecha y hora que puede ser nulo y en blanco, se utiliza para la fecha de finalización de la tarea
    important = models.BooleanField(default=False)
    # Un campo booleano que indica si la tarea es importante o no, con un valor predeterminado de False
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Un campo de clave externa que establece una relación muchos a uno con el modelo User, indicando que cada tarea pertenece a un usuario

    def __str__(self):
        return self.title + ' - ' + self.user.username
    # Método que devuelve una representación legible de la tarea, en este caso, el título de la tarea seguido del nombre de usuario del propietario de la tarea
