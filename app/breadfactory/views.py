from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    OrderSerializer,
    OrdererSerializer,
    ItemSerializer,
    FactorSerializer,
    ProductionSerializer
)

from .models import (
    Orders,
    Factors,
    Orderers,
    Production,
    Items
)


class ItemApiView(APIView):
    def get(self, request):
        try:
            model = Items.objects.all()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderApiView(APIView):
    def get(self, request):
        try:
            model = Orders.objects.all()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class FactorApiView(APIView):
    def get(self, request):
        try:
            model = Factors.objects.all()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FactorSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FactorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductionApiView(APIView):
    def get(self, request):
        try:
            model = Production.objects.all()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductionSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrdererApiView(APIView):
    def get(self, request):
        try:
            model = Orderers.objects.all()
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = OrdererSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrdererSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
