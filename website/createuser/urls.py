from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'createuser'
urlpatterns = [
    #path('', views.get_user, name='index'),
    url(r'^/$',views.get_user),
]
