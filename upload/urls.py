from django.urls import path
from . import views

app_name='upload'

urlpatterns = [
    path('', views.upload, name='upload'),
    path('process-image/', views.process_image, name='process_image'),
]
