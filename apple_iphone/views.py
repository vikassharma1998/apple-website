from django.shortcuts import render, redirect
from .models import IphoneModels,IphoneFeatures
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets 
from .serializers import ItemSerializer, FeaturesSerializer
from rest_framework import generics
# Create your views here.

# index Function
def index(request):
    iphone_models = IphoneModels.objects.all()      # get all data from iphone_models
    Iphone_Features = IphoneFeatures.objects.all()      # get all data from iphone_features
    return render(request, "apple_iphone/index.html", {'iphone_models' : iphone_models,'Iphone_Features': Iphone_Features})

#Register Function
def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']
        conf_password = request.POST['conf_password']
        email = request.POST['email']
        username = request.POST['username']
        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                print("Username Taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                print("Email Taken")    
            else:    
                user = User.objects.create_user(first_name=first_name, last_name=last_name, password=password, email=email, username=username)
                user.save()
                messages.info(request,'User Created')
                print("User Created")
        else:
            print("error")
            return render(request, "apple_iphone/index.html")
    else:
        return render(request, "apple_iphone/index.html")

    return render(request, "apple_iphone/index.html")    

# login Function
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("login Done")
            messages.info(request,"login Done")
            return redirect("/")

        else:
            print("error")
            messages.info(request, 'Invalid credentials')
            return redirect("/")

    else:
        messages.info(request, 'Invalid credentials')
        return render(request, "apple_iphone/index.html")

# logout Function
def logout(request):
    iphone_models = IphoneModels.objects.all()
    Iphone_Features = IphoneFeatures.objects.all()
    auth.logout(request)
    messages.info(request,"Logout Done")
    return render(request, "apple_iphone/index.html", {'iphone_models' : iphone_models,'Iphone_Features': Iphone_Features})



def query(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        mobile_number = request.POST['mobile_number']
        email = request.POST['email_id']
        subject= request.POST['email_id']
        user_message = request.POST['user_message']
        message = f'Name: {first_name} {last_name}\nMobile Number: {mobile_number}\n Email: {email}\n query: {user_message} '
        email_from = settings.EMAIL_HOST_USERviews.postlist.as_view  


class GetFeature(generics.ListAPIView):
    queryset = IphoneFeatures.objects.all()
    serializer_class = FeaturesSerializer

@api_view(['GET'])
def getDataIphoneModels(request):
    items = IphoneModels.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def GetDataIphoneFeatures(request):
    items = IphoneFeatures.objects.all()
    serializer = FeaturesSerializer(items, many=True)
    return Response(serializer.data)    

# @api_view(['POST'])
# def addmodels(request):
#     serializer = ItemSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)    

# @api_view(['POST'])
# def addFeatures(request):
#     serializer = FeaturesSerializer(data=request.data)
#     print(serializer)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)    


class addFeatures(generics.ListCreateAPIView):
    queryset = IphoneFeatures.objects.all()
    serializer_class = FeaturesSerializer


class addmodels(generics.ListCreateAPIView):
    queryset = IphoneModels.objects.all()
    serializer_class = ItemSerializer    
