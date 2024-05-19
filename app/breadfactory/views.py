from rest_framework import viewsets
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


class ItemApiView(APIView):
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
