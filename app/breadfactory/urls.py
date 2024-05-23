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
    path('item/<int:pk>/', ItemApiView.as_view(), name='Удаление изделия'),

    path('order/', OrderApiView.as_view(), name='Добавление заказа'),
    path('order/<int:pk>/', OrderApiView.as_view(), name='Удаление заказа'),

    path('orderer/', OrdererApiView.as_view(), name='Доблание заказчика'),
    path('orderer/<int:pk>/', OrdererApiView.as_view(), name='Удаление заказчика'),

    path('factor/', FactorApiView.as_view(), name='Добаление производственного цеха'),
    path('factor/<int:pk>/', FactorApiView.as_view(), name='Удаление производственного цеха'),

    path('production/', ProductionApiView.as_view(), name='Добавление цеха'),
    path('production/<int:pk>/', ProductionApiView.as_view(), name='Удаление цеха'),

]
