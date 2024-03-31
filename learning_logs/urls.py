from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('check_topics/', views.topics, name="check_topics"),
    path('topic/<topic_id>/', views.topic, name='topic'),
]