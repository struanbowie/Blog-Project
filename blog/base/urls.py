from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('desk/<str:pk>/', views.desk, name="desk"),

	path('create-desk/', views.createDesk, name="create-desk"),
	path('update-desk/<str:pk>/', views.updateDesk, name="update-desk"),
	path('delete-desk/<str:pk>/', views.deleteDesk, name="delete-desk"),
	]