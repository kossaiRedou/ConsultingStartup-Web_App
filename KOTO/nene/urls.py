from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path





urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    
    path('blog/', views.blog, name='blog'),
    path("article/<slug:slug>/", views.blog_detail, name="blog_detail"),
    
    path('contact/', views.contact_view, name='contact'),
    
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio-details/', views.portfolio_details, name='portfolio-details'),
    
    path('pricing/', views.pricing, name='pricing'),
    
    path('service-details/', views.service_details, name='service-details'),
    
    path('services/', views.services, name='services'),
    
    path('starter-page/', views.starter_page, name='starter-page'),
    
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonials, name='testimonials'),
]

# Ajoute cette ligne pour servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)