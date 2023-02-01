from django.db import router
from . import views
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers

# router= routers.DefaultRouter()
# router.register('addmodels',views.aaddFeatures)

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('query', views.query, name='query'),
    path('getFeature/', views.GetFeature.as_view()),
    path('getFeatures', views.GetDataIphoneFeatures),
    path('getModels', views.getDataIphoneModels),
    path('addmodels', views.addmodels.as_view()),
    path('addFeatures', views.addFeatures.as_view()),
]
