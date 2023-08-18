from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer



# Create your views here.
@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)



@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    # here we create a serializer and give it the product object which converts it to a python dictionary 
    serializer = ProductSerializer(product)
    #serializer.data gives us the dictionary
    return Response(serializer.data)
    