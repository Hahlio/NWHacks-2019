from django.urls import path

from . import views

urlpatterns = [
    # profile/username/fb
    path('username/fb/', views.fbCreateOrLogin),
    # profile/username/
    path('username/', views.lookupUser),
    # profile/id
    path('<int:task_id>', views.handle_existing_task),
    # profile/notification/<id>
    path('notification/<int:profile_id>', views.notify),
    # profile/
    path('', views.createProf),
]