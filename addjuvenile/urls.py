from django.urls import path
from . import views

app_name = 'addjuvenile'

urlpatterns = [
    path('', views.add_juvenile, name='add_juvenile'),
]
