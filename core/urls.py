from django.urls import path

from .views import index, contact, product, client

urlpatterns = [
    path('', index, name='index'),
    path('contato', contact, name='contato'),
    path('produto/<int:pk>', product, name='produto'),
    path('cliente/<int:pk>', client, name='cliente')
]
