from django.urls import path

from products.views import ProductsListView, ProductsDetailView, ProductsDetailFieldView

urlpatterns = [
    path("", ProductsListView.as_view(), name="all-products"),
    path("<str:latinos_name>/", ProductsDetailView.as_view(), name="detail-products"),
    path(
        "<str:latinos_name>/<str:field_name>/",
        ProductsDetailFieldView.as_view(),
        name="detail-products-fields"
    ),
 ]
app_name = "products"
