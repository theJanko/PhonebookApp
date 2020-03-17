from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('detail/<int:person_id>/', views.detail, name='detail'),
    path('contacts/', views.contact_list, name='contact-list'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
    path('<int:person_id>/phone_number', views.phone_number, name='phone_number'),

]
