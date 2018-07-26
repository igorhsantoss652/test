from django.urls import path
from .views import clients
from .views import client_new
from .views import client_update
from .views import client_delete
urlpatterns = [
    path('', clients, name="clients"),
    path('new/', client_new, name="client_new"),
    path('update/<int:id>', client_update, name="client_update"),
    path('delete/<int:id>', client_delete, name="client_delete"),
]