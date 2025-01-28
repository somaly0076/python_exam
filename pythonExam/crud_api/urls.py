from django.urls import path
from .views import get_product,create_category,create_product,get_category

urlpatterns =[
    path('products/', get_product,name='get_product'),
    path('products/create', create_product,name='create_product'),
    path('categories/',get_category,name='get_category'),
    path('categories/create',create_category,name ='create_category')
]