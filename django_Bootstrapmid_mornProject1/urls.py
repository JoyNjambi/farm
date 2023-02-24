"""django_Bootstrapmid_mornProject1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from django_Bootstrapmid_mornProject1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='my-index'),
    path('about/',views.about, name='about-page'),
    path('blog/',views.blog, name='my-blog'),
    path('contact/',views.contact, name='my-contact'),
    path('detail',views.detail, name='my-details'),
    path('feature/',views.feature, name='my-feature'),
    path('product/',views.product, name='my-product'),
    path('service/',views.service, name='my-services'),
    path('team/',views.team, name='my-team'),
    path('testimonial/',views.testimonial, name='my-testimonial'),


]
