from django.urls import path

from . import views

urlpatterns = [
    path('<int:goal_id>/', views.handle_goal),
]