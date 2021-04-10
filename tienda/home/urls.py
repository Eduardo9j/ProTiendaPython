from django.urls import path
from .views import about_view
from .views import contacto_view

urlpatterns=[
    path('about/', about_view, name='about_view'),
    path('contacto/', contacto_view, name='contacto_view'),
]