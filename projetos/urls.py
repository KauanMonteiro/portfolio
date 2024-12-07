from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('download/exe/<int:projeto_id>/', views.download_exe, name='download_exe'),
    path('download/linux/<int:projeto_id>/', views.download_linux, name='download_linux'),
    path('download/apk/<int:projeto_id>/', views.download_apk, name='download_apk'),
]
