from django.urls import path
from . import views

urlpatterns = [
    path('donors/', views.donor_list, name='donor_list'),
    path('', views.home, name='home'),
    path('donations/', views.my_view, name='donations'),


]
