from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.baseview, name='index'),
    path('map/', views.FoliumView.as_view(), name='map'),
]