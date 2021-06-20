from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('register', views.AppViewSet.as_view({'post': 'register'})),
    path('login', views.AppViewSet.as_view({'post': 'login'})),
    path('getUserinfo', views.AppViewSet.as_view({'get': 'getUserinfo'})),
    path('logout', views.AppViewSet.as_view({'post': 'logout'})),
    path('updateUserinfo', views.AppViewSet.as_view({'post': 'updateUserinfo'})),
    path('getGoodslist', views.AppViewSet.as_view({'post': 'getGoodslist'})),
    path('uploadimg', views.AppViewSet.as_view({'post': 'uploadimg'})),
    path('getOneGoods', views.AppViewSet.as_view({'post': 'getOneGoods'})),
    path('getChartdata', views.AppViewSet.as_view({'post': 'getChartdata'})),
    path('addgoods', views.AppViewSet.as_view({'post': 'addgoods'})),
    path('getprice', views.AppViewSet.as_view({'post': 'getprice'})),
    path('generate_order', views.AppViewSet.as_view({'post': 'generate_order'})),
    path('getOrderlist', views.AppViewSet.as_view({'post': 'getOrderlist'})),
    path('updateavatar', views.AppViewSet.as_view({'post': 'updateavatar'})),
]