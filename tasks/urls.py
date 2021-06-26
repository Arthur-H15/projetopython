
from django.urls import path
from . import views
urlpatterns = [
    path('Ola/', views.Ola),   
    path("",views.tasklist,name='task-list') ,
    path("yourname/<str:name>",views.yourname,name='yourname')
]