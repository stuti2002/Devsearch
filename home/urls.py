from django.contrib import admin
from django.urls import path
from home import views
from home.views import  DeleteProject

urlpatterns = [
    path('',views.singleproject,name='singleproject'),
    path('singleproject/',views.singleproject,name='singleproject'),
    path('project/<str:pk>/',views.project,name='project'),
    path('project_form/',views.CreateProject,name='project_form'),
    path('update_project/<str:pk>/',views.UpdateProject,name='update_project'),
    path('delete_project/<str:pk>/',views.DeleteProject,name='delete_project'),
]