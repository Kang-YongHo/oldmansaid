"""oldmansaid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import MyModelListView, MyModelCreateView, MyModelDetailView, MyModelUpdateView, MyModelDeleteView

urlpatterns = [
    path('', MyModelListView.as_view(), name='index'),
    path('create/', MyModelCreateView.as_view(), name='create'),
    path('read/<int:pk>/', MyModelDetailView.as_view(), name='read'),
    path('update/<int:pk>/', MyModelUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MyModelDeleteView.as_view(), name='delete'),
]
