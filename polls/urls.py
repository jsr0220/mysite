
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results),
    path('<int:question_id>/vote/', views.votes),
]
