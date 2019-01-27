from django.urls import path

from . import views

urlpatterns = [
    path('', views.handle_new_user),
    path('/<str:username', views.handle_username),
    path('/<int:user_id>/', views.handle_user),
    path('/<int:user_id>/ical/', views.handle_user_ical),
    path('/<int:user_id>/task', views.handle_user_task),
    path('/<int:user_id>/goal/<int:goal_id>/task', views.handle_user_goal_task),
]