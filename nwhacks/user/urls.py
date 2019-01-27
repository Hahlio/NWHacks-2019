from django.urls import path

from . import views

urlpatterns = [
    path('<str:username>', views.handle_username),
    path('<int:user_id>/ical', views.handle_user_ical),
    path('task/<int:user_id>/', views.handle_user_task),
    path('id/<int:user_id>', views.handle_user_id),
    path('goal/<int:user_id>', views.handle_user_goal),
    path('goal/<int:user_id>/task/<int:goal_id>', views.handle_user_goal_task),
]