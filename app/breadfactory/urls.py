from django.contrib import admin
from django.urls import path
from .views import ItemApiView

urlpatterns = [
    path('item/', ItemApiView.as_view(), name='Добавление изделия'),
]
