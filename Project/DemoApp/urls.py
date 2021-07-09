from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path("timelog", views.timelog),
    path("locationlog", views.locationlog),
    path("reg", views.reg),
    path("update", views.update),
    path("hi.html", views.hi),
    path('lo', views.lo),
    path('login', views.login),
    path('hi', views.hello),
    path('style.css', views.sty),
    path('', views.index,name='index'),
    path('index', views.index,name='index'),
]