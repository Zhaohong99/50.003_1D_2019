from django.urls import path

from . import views

app_name = 'Profile'
urlpatterns = [
    path('viewProfile/', views.view_profile, name='viewProfile'),
]