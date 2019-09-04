from django.shortcuts import render ,get_object_or_404
from .models import  Category,Product
from cart.forms import CartAddProductForm
from .shop_api import Shopserializer, CategorySerializer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


# Create your views here.
def product_list(request,category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        products = products.filter(category=category)
    args = {'category':category, 'categories':categories, 'products':products}
    return render(request,'shop/product/list.html',args)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    args = {'product': product, 'cart_product_form': CartAddProductForm()
}
    return render(request,'shop/product/detail.html', args)


@api_view(['GET', 'POST'])
def cat_list(request):
    if request.method == 'GET':
        cat = Category.objects.all()
        ser = Shopserializer(cat,many=True)
        return JsonResponse(ser.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Shopserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@api_view(['POST'])
def create_cat(request):
    data = JSONParser().parse(request)
    serializer = CategorySerializer(data=data)
    print ("Tunde ser -----",serializer.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)


# https://medium.com/quick-code/token-based-authentication-for-django-rest-framework-44586a9a56fb
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    print ("TUNDE ",request.POST)
    print ("Tunde ",request.data,request.data['username'])
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    print ("User ---", user)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},status=HTTP_200_OK)

