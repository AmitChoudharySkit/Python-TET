from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login , logout

@api_view(['GET'])
def get_products(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product , many = True)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    if request.user.is_anonymous:
        print("user is anonymous")
        return redirect("login")
    else:
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED )
        return Response(serializer.errors ,  status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def product_detail(request , pk):
    if request.user.is_anonymous:
        return redirect("login")
    else:
        try:
            product = Product.objects.get(pk = pk)
        except Product.DoesNotExist:
            return Response(status= status.HTTP_404_NOT_FOUND)
    
        if request.method == 'GET' :
            serializer = ProductSerializer(product)
            return Response(serializer.data)
    
        elif request.method == 'PUT':
            serializer = ProductSerializer(product , data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data , status = status.HTTP_201_CREATED )
            return Response(serializer.errors ,  status = status.HTTP_400_BAD_REQUEST)
    
        elif request.method == 'DELETE':
            product.delete()
            return Response(status= status.HTTP_204_NO_CONTENT)
    
def index(request):
    if request.user.is_anonymous:
        return redirect("login")
    return render(request,'index.html')

def loginUser(request):
    if request.method == "POST":
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        user = authenticate(username=Username, password=Password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else: 
            return render(request,'login.html')  

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("login")