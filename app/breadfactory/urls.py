from django.contrib import admin
from django.urls import path
from .views import (
    OrderApiView,
    ItemApiView,
    OrdererApiView,
    FactorApiView,
    ProductionApiView
)

urlpatterns = [
    path('item/', ItemApiView.as_view(), name='Добавление изделия'),
    path('order/', OrderApiView.as_view(), name='Добавление заказа'),
    path('orderer/', OrdererApiView.as_view(), name='Доблание заказчика'),
    path('factor/', FactorApiView.as_view(), name='Добаление производственного цеха'),
    path('production/', ProductionApiView.as_view(), name='Добавление цеха'),
]
