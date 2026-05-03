from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.appointments_list, name='appointments_list'),
    path('appointments/update/<int:pk>/', views.update_appointment, name='update_appointment'),
]
