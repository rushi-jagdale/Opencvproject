"""C360Software URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls.conf import include
from c360app import views
# admin.site.site_header = "C360Software"
# admin.site.site_title = "Welcome to C360Software"
urlpatterns = [
    path('login/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('Receptionist/login/',views.Receptionist,name='login'),
    path('emplogin/',views.emplogin,name='emplogin'),
    path('empadd/',views.empadd,name='empadd'),

    # path('register',include('c360app.urls')),
    path('', views.index, name='index'),
    path('video_stream/', views.video_stream, name='video_stream'),
    path('add_photos/', views.add_photos, name='add_photos'),
    path('add_photos/<slug:emp_id>/', views.click_photos, name='click_photos'),
    path('train_model/', views.train_model, name='train_model'),
    path('detected/', views.detected, name='detected'),
    path('identify/', views.identify, name='identify'),
    path('add_emp/', views.add_emp, name='add_emp'),
]