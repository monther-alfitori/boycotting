from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('articles/', views.articles, name="articles"),
    path('article/<str:pk>', views.article, name="article"),
    path('phrases/', views.phrases, name="phrases"),
    path('boycotting/', views.boycotting, name="boycotting"),
    path('alternatives/', views.alternatives, name="alternatives"),
    path('product/<str:pk>/', views.product, name="product"),
    path('shares/', views.shares, name="shares"),
    path('boycotters/', views.boycotters, name="boycotters"),
    path('boycotter/<str:pk>/', views.boycotter, name="boycotter"),

]