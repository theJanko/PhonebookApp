from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('<int:person_id>/', views.detail, name='detail'),
    path('contacts/', views.contact_list, name='contact-list'),
    path('delete/<int:person_id>/', views.delete, name='delete'),
    path('edit/<int:person_id>/', views.edit, name='edit'),
    path('search/', views.search, name='search_results'),

]
