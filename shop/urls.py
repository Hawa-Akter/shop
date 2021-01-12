from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/', views.category_list, name='category_list'),


]
