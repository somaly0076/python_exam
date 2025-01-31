from django.urls import path
from .views import get_product,create_category,create_product,get_category,update_product,delete_product,update_category,delete_category, search_for_image

urlpatterns =[
    # api endpoint for ProductTB
    path('products/', get_product,name='get_product'),
    # To Create Product with image upload, you can use Postman
    path('products/create', create_product,name='create_product'),
    path('products/update/<int:pk>',update_product,name='update_product'),
    path('products/delete/<int:pk>',delete_product,name = 'delete_product'),
    
    # api endpoint for CategoryTB
    path('categories/',get_category,name='get_category'),
    path('categories/create',create_category,name ='create_category'),
    path('categories/update/<int:pk>',update_category,name='update_category'),
    path('categories/delete/<int:pk>',delete_category,name = 'delete_category'),

    # api endpoint for Search Engine
    path('image_search/',search_for_image ,name='image_serch')
]