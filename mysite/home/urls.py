from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('home', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('itemlist', views.itemlist, name = 'itemlist'),
    path('contact', views.contact, name = 'contact')
]

# STATICFILES_DIRS = [
#     path('static', views.static, name = 'static')
# ]