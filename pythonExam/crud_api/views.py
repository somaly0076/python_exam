from django.shortcuts import render
from PIL import Image
import os
from DeepImageSearch import Load_Data, Search_Setup
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ProductTB, CategoryTB
from .serializer import ProductSerializer, CategorySerializer
# Create your views here.

#create product function
@api_view(['POST'])
def create_product(request):
    data = request.data.copy()
    data.update(request.FILES)
    serializer = ProductSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

#get all product or search by id, name or image function
@api_view(['GET'])
def get_product(request,*args,**kwargs):
    products = ProductTB.objects.all()
    search_id = request.query_params.get('id',None)
    search_name = request.query_params.get('name',None)
    search_image = request.query_params.get('image',None)
    if search_id:
        product = products.filter(id=search_id)
        prod_serializer = ProductSerializer(product,many = True)
        return Response(prod_serializer.data)
    elif search_name:
        product = products.filter(name__contains=search_name)
        prod_serializer = ProductSerializer(product,many = True)
        return Response(prod_serializer.data)
    elif search_image:
        product = products.filter(image=search_image)
        prod_serializer = ProductSerializer(product,many = True)

    prods_serializer = ProductSerializer(products,many = True)
    return Response(prods_serializer.data)

#update product by id function
@api_view(['PUT'])
def update_product(request,pk):
    product = ProductTB.objects.get(id=pk)
    prod_serializer = ProductSerializer(product, data=request.data)
    if prod_serializer.is_valid():
        prod_serializer.save()
    return Response(prod_serializer.data)

#delete product by id function
@api_view(['DELETE'])
def delete_product(request,pk):
    product = ProductTB.objects.get(id=pk)
    product.delete()
    return Response('Product is deleted successfully!')

#get all category included products, search by id or name function
@api_view(['GET'])
def get_category(request):
    categories = CategoryTB.objects.all()
    search_id = request.query_params.get('id',None)
    search_name = request.query_params.get('name',None)
    if search_id:
        category = categories.filter(id=search_id)
        categ_serializer = CategorySerializer(category,many = True)
        return Response(categ_serializer.data)
    elif search_name:
        category = categories.filter(name__contains=search_name)
        categ_serializer = ProductSerializer(category,many = True)
        return Response(categ_serializer.data)
    categ_serializer = CategorySerializer(categories,many = True)
    return Response(categ_serializer.data)

#create category function
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

#update category by id function
@api_view(['PUT'])
def update_category(request,pk):
    category = CategoryTB.objects.get(id=pk)
    categ_serializer = CategorySerializer(category, data=request.data)
    if categ_serializer.is_valid():
        categ_serializer.save()
    return Response(categ_serializer.data)

#delete category by id function
@api_view(['DELETE'])
def delete_category(request,pk):
        category = CategoryTB.objects.get(id=pk)
        category.delete()

        return Response('Category is deleted successfully!')

# search for similar image function. It is not yet worked as I have tried with my best efford as well as I am new to this library. I am looking forward to learn more and fix on this issue. 
def search_for_image(request):
    uploaded_path = ''
    if request.method == "POST":
        img_to_search = request.FILES.get('img_to_search')
        img = Image.open(img_to_search)
        file_name = img_to_search.name  # Use 'name' to get the actual file name
        #create the file path to save in uploaded_img folder
        uploaded_path = os.path.join("crud_api/static/uploaded_img", file_name)
        os.makedirs(os.path.dirname(uploaded_path), exist_ok=True)
        img.save(uploaded_path)
        # remove 'crud_api/static/' path to display in img tag otherwise the file is not found
        uploaded_path = uploaded_path.replace('crud_api/static/','')
      

    image_list = Load_Data().from_folder(['crud_api/static/img'])
    images = Search_Setup(image_list=image_list, model_name='vgg19', pretrained=True, image_count=100)

    # it stated with the keyError with the code below
    # images.run_index()

    if uploaded_path != '':
        for ind, img in enumerate(image_list):
            image_list[ind] = img.replace('crud_api/static','')

        # it cannot file the file path for the code below
        
        # uploaded_path = 'static/' + uploaded_path.replace('\\', '/')
        # image_list = images.get_similar_images(image_path = uploaded_path, number_of_images = 10) 
      

    return render(request,'image_search_engine.html',{
        "img_to_search": uploaded_path,
        "image_list": image_list
    })
