from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Product
from ..serializers import ProductSerializer

# Create your views here.


@api_view(["GET"])
def product_list(reuqest):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(
            {"message": "Product does not exist"},
            status=status.HTTP_404_NOT_FOUND,
        )
