# coding=utf-8
# django libs
from django.urls import path, include

# 3rd party libs
from rest_framework.routers import DefaultRouter

# custom import
from . import views

# Namespace for URLs in this users app
app_name = 'general'
router = DefaultRouter()
# router.register('', views.ViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_qr/', views.generate_qr, name='generate_qr'),
    path('api/', include(router.urls)),
]

# when user go to path /app_name/ it will show api root page (endpoints list)
urlpatterns += router.urls
