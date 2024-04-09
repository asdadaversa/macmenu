import datetime

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Products
from products.serializers import ProductsSerializer


class ProductsListView(APIView):
    """ APIVIEW for lista """

    serializer_class = ProductsSerializer

    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
