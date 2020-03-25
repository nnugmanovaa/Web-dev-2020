from django.urls import  path
from api import  views
from api.views import product_list, product_detail, get_category_detail, get_category_list,get_products_from_category

urlpatterns = [
    path('products/', product_list),
    path('products/<int:product_id>/', product_detail),
    path('categories/',get_category_list),
    path('categories/<int:category_id>/', get_category_detail),
    path('categories/<int:id>/products/', get_products_from_category),
]