from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),
    path('goodbye', views.goodbye_world, name='goodbye_world'),
]
