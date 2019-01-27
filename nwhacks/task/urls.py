from django.urls import path

from . import views

urlpatterns = [
    path('<int:task_id>', views.handle_existing_task),
]