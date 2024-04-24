from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from django.core.cache import cache

@api_view(['GET'])
def product_list(request):
    # products = Product.objects.all()
    # serializer = ProductSerializer(products, many=True)
    # json_response = serializer.data
    # return Response(json_response)

    cache_key = 'product_list'

    if not cache.get(cache_key):
        print('cache_miss')
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_response = serializer.data
        cache.set(cache_key, json_response, 60)
    
    response_data = cache.get(cache_key)
    return Response(response_data)