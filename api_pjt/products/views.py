from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product

class ProductListAPIView(APIView):

    def get(self, request):
        cache_key = "product_list"
        
        if not cache.get(cache_key):
            print("cache miss")
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            json_response = serializer.data
            cache.set(cache_key, json_response, 180)

        response_data = cache.get(cache_key)
        return Response(response_data)
