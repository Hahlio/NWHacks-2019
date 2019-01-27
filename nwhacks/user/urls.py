from django.urls import path

from . import views

urlpatterns = [
    path('/<int:user_id>/', views.handle_user),
    path('', views.handle_new_user),
]