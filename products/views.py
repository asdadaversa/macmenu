from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Products
from products.serializers import ProductsSerializer


class ProductsListView(APIView):
    """ APIVIEW for list products """

    serializer_class = ProductsSerializer

    def get(self, request, format=None):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsDetailView(APIView):
    """ APIVIEW for detail products by latinos_name """

    def get(self, request, latinos_name, field_name=None, format=None):
        product = get_object_or_404(Products, latinos_name=latinos_name)
        serializer = ProductsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsDetailFieldView(APIView):
    """ APIVIEW for detail products by latinos name and fields """

    def get(self, request, latinos_name, field_name=None, format=None):
        product = get_object_or_404(Products, latinos_name=latinos_name)
        if field_name:
            try:
                field_value = getattr(product, field_name)
                return Response({field_name: field_value}, status=status.HTTP_200_OK)
            except AttributeError:
                return Response(
                    {"error": f"Field '{field_name}' does not exist"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            serializer = ProductsSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
