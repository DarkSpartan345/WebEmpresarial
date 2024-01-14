from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('blog/', views.blog,name="blog"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('sample/', views.sample,name="sample"),
    path('services/', views.services,name="services"),
    path('store/', views.store,name="store"),
]   