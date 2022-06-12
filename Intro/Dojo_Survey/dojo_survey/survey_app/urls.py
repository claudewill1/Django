from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('return_home',views.index),
    path('result',views.result)
]