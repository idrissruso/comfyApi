from django.http.response import JsonResponse
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product
import random 

# Create your views here.
def home(request):
    return JsonResponse({"message": "welcome to the home page"})

@api_view(['POST'])
def create_product(request):
    if request.method == "POST":
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "success", "status": status.HTTP_201_CREATED, "product": serializer.data,}
            return JsonResponse(response, status=status.HTTP_201_CREATED)
        response = {"message": "failed", "status": status.HTTP_400_BAD_REQUEST, "product": serializer.errors,}
        return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def get_product_by_page(request, page):
    if request.method == "GET":
        products = Product.objects.all()
        page_size = 15
        start = page_size * (page - 1)
        end = page_size * page
        serializer = ProductSerializer(products[start:end], many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"products": serializer.data,}
        return JsonResponse(response, safe=False)


@api_view(['GET'])
def get_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"products": serializer.data,}
        return JsonResponse(response, safe=False)
    
@api_view(['POST'])
def create_products(request):
    if request.method == "POST":
        data = request.data
        for product in data:
            serializer = ProductSerializer(data=product)
            if serializer.is_valid():
                serializer.save()
            else:
                response = {"message": "failed", "status": status.HTTP_400_BAD_REQUEST, "product": serializer.errors,}
                return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        response = {"message": "success", "status": status.HTTP_201_CREATED,}
        return JsonResponse(response, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_featured_products(request):
    if request.method == "GET":
        products = Product.objects.all()
        featured_products = random.sample(list(products), 3)
        serializer = ProductSerializer(featured_products, many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"products": serializer.data,}
        return JsonResponse(response, safe=False)
    
@api_view(['GET'])
def get_product_by_id(request, id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        response = {"message": "success", "status": status.HTTP_200_OK,"product": serializer.data,}
        return JsonResponse(response, safe=False)


@api_view(['GET'])
def get_product_by_category_page(request, category, page):
    if request.method == "GET":
        products = Product.objects.filter(category=category)
        page_size = 15
        start = page_size * (page - 1)
        end = page_size * page
        serializer = ProductSerializer(products[start:end], many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"products": serializer.data,}
        return JsonResponse(response, safe=False)
    
@api_view(['GET'])
def get_product_by_category(request, category):
    if request.method == "GET":
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"products": serializer.data,}
        return JsonResponse(response, safe=False)  