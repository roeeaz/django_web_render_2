from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', views.index),
    path('imgs/<pk>', views.MyModelView.as_view()),
    path('imgs/', views.MyModelView.as_view()),
    path('students/', views.student_Views.as_view()),
    path('test/', views.test),
    path('login/', TokenObtainPairView.as_view()),
    path('register/', views.register),
]
