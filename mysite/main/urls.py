from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('news/', views.articles, name="articles"),
    path('phrases/', views.phrases, name="phrases"),
    path('boycotting/', views.boycotting, name="boycotting"),
    path('alternatives/', views.alternatives, name="alternatives"),
    path('shares/', views.shares, name="shares"),
    path('boycotters/', views.boycotters, name="boycotters"),
    path('boycotter/<str:pk>/', views.boycotter, name="boycotter"),

]