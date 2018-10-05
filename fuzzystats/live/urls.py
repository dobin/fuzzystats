from django.urls import path, re_path
from . import views

urlpatterns = [
    path('list/', views.fuzzingrun_list, name='fuzzingrun_list'),
    path('', views.fuzzingrun_latest, name='fuzzingrun_latest'),

    path(r'api/fuzzingruns/', views.fuzzingrun_list),
    re_path(r'api/fuzzingruns/(?P<pk>[0-9]+)/', views.fuzzingrun_detail),
]
