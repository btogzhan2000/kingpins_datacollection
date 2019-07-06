from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^register/', views.register, name= 'register'),
    url(r'^login/', views.login, name= 'login'),
	url(r'^logout/', views.logout, name= 'logout'),
	url(r'^home/', views.logout, name= 'home')
]