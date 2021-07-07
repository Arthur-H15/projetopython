
from django.urls import path
from . import views
urlpatterns = [
    path('Ola/', views.Ola),   
    path("",views.tasklist,name='task-list') ,
    path("yourname/<str:name>",views.yourname,name='yourname'),
    path("task/<int:id>",views.taskview,name='taskview'),
    path("novatarefa/" ,views.newTask,  name='newtask'),
    path("edit/<int:id>" , views.edittask, name='edittask'),
    path("delete/<int:id>" , views.deletetask, name='delitetask'),
    path("trocarStatus/<int:id>" , views.trocarStatustask, name='trocarStatustask'),
    

]