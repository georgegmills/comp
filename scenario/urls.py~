from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Representatives$', views.RepView.as_view(), name='rep_list'),
]
