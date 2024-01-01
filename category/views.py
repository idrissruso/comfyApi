from django.http.response import JsonResponse
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Category
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return JsonResponse({"message": "welcome to the home page"})

@csrf_exempt
@api_view(['POST'])
def create_category(request):
    if request.method == "POST":
        data = request.data
        print(data)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "success", "status": status.HTTP_201_CREATED, "category": serializer.data,}
            return JsonResponse(response, status=status.HTTP_201_CREATED)
        response = {"message": "failed", "status": status.HTTP_400_BAD_REQUEST, "category": serializer.errors,}
        return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        response = {"message": "success", "status": status.HTTP_200_OK,"categories": serializer.data,}
        return JsonResponse(response, safe=False)