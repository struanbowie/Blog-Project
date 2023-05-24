from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('desk/<str:pk>/', views.desk, name="desk"),
]