"""joga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from . import views

app_name = 'joga_app'

urlpatterns = [
    path('submit_comment', views.submit_comment, name="submit_comment"),
    path('post/<int:post_id>/', views.post, name="post"),
    path('lesson/<int:lesson_id>/', views.lesson, name="lesson"),
    path('location/<int:location_id>/', views.location, name="location"),
    path('ajax_load_more_blog/', views.blog, name="ajax_blog"),
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('lessons/', views.lessons, name="lessons"),
    path('about_me/', views.about_me, name="about_me"),
    path('recipes/', views.recipes, name="recipes"),
    path('events/', views.events, name="events"),
]
