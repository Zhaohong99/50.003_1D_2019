from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'login'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('log_out/', views.log_out, name='logout')
    url(r'^$', views.index)
]
