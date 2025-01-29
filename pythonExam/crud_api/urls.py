from django.urls import path
from .views import get_product,create_category,create_product,get_category,update_product,delete_product,update_category,delete_category

urlpatterns =[
    path('products/', get_product,name='get_product'),
    path('products/create', create_product,name='create_product'),
    path('products/update/<int:pk>',update_product,name='update_product'),
    path('products/delete/<int:pk>',delete_product,name = 'delete_product'),

    path('categories/',get_category,name='get_category'),
    path('categories/create',create_category,name ='create_category'),
    path('categories/update/<int:pk>',update_category,name='update_category'),
    path('categories/delete/<int:pk>',delete_category,name = 'delete_category'),
]