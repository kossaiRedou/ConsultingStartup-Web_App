from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/', views.blog_details, name='blog-details'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    path('pricing/', views.pricing, name='pricing'),
    path('service-details/', views.service_details, name='service-details'),
    path('services/', views.services, name='services'),
    path('starter-page/', views.starter_page, name='starter-page'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
]