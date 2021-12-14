from django.urls import path
from users import views
from users.views import  Profiles

urlpatterns = [
    path('',views.Profiles,name='Profiles'),
]
