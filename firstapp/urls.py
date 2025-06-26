from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('contact/list/', views.contact_list, name="contact_list"),
    path('contact/delete/<int:pk>/', views.contact_delete, name="contact_delete"),
    path('contact/edit/<int:pk>/', views.contact_edit, name="contact_edit"),
]