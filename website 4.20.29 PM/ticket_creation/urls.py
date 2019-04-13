from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'ticket_creation'
urlpatterns = [
    path('', views.create, name='create'),
    path('display/', views.list, name='display'),
    path('delete/', views.delete, name='delete'),
    path('detail/', views.detail, name='detail'),
    path('resolve/', views.resolve, name='resolve'),
    path('remote_create/', views.remote_create, name='remote_create'),

    path("",
        TemplateView.as_view(template_name="application.html"),
        name="app",
    ),
]
