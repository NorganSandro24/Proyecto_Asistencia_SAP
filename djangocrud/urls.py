from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('', views.home, name='home'),
    # Ruta para la página de inicio del sitio
    path('admin/', admin.site.urls),
    # Ruta para acceder al panel de administración de Django
    path('signup/', views.signup, name='signup'),
    # Ruta para la página de registro de usuarios
    path('tasks/', views.tasks, name='tasks'),
    # Ruta para la página de listado de tareas
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    # Ruta para la página de listado de tareas completadas
    path('logout/', views.signout, name='logout'),
    # Ruta para cerrar sesión de un usuario
    path('signin/', views.signin, name='signin'),
    # Ruta para la página de inicio de sesión
    path('create_task/', views.create_task, name='create_task'),
    # Ruta para la página de creación de una nueva tarea
    path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    # Ruta para ver los detalles de una tarea específica
    path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    # Ruta para marcar una tarea como completada
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    # Ruta para eliminar una tarea
]
