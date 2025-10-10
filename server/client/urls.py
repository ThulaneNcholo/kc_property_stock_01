
from django.urls import path
from .import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('about-us', views.AboutUsView, name='about-us'),
    path('sellers', views.SellersView, name='sellers'),
    path('rental-agent', views.RentalView, name='rental-agent'),
    path('properties', views.PropertiesView, name='properties'),
    path('services', views.ServicesView, name='services'),
    path('contact-us', views.ContactView, name='contact-us'),
    path('property-areas',
         views.PropertyAreasView, name='property-areas'),
    path('private-properties', views.PrivatePropertiesView,
         name='private-properties'),
]
