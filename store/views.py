from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer



# Create your views here.
@api_view()
def product_list(request):
    return Response('ok')



@api_view()
def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        # here we create a serializer and give it the product object which converts it to a python dictionary 
        serializer = ProductSerializer(product)
        #serializer.data gives us the dictionary
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    