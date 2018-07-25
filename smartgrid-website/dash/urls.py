from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.dash, name='dash'),
    
    # ex: /dash/dash_statistics_mean/
    path('dash_statistics_mean/', views.dash_statistics_mean, name='dash_statistics_mean'),

    # ex: /dash/mean_statistic/?metric=consumption&data=neighborhood
    re_path(r'^mean_statistic/$', views.mean_statistic, name='mean_statistic'),

    # ex: /dash/visualization/
    path('visualization/', views.visualization, name='visualization'),
]
