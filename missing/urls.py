from django.urls import path
from . import views

app_name = 'missing'

urlpatterns = [
    path('', views.missing, name='missing'),
    path('juvenile_details/<int:id>/', views.juvenile_details, name='juvenile_details'),
    path('set_missing/<int:id>/', views.set_missing, name='set_missing'),
    path('set_found/<int:id>/', views.set_found, name='set_found'),
    path('delete_record/<int:id>/', views.delete_record, name='delete_record'),
]
