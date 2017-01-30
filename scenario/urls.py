from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Representatives$', views.RepView, name='rep_list'),
    url(r'^Plans$', views.PlanView, name='plan_list'),
]
