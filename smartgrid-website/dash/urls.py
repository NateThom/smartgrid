from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.dash, name='dash'),

    # ex: /dash/dash_statistics_mean/
    path('dash_statistics_mean/', views.dash_statistics_mean, name='dash_statistics_mean'),

    # ex: still need to discover
    re_path(r'^mean_statistic/$', views.mean_statistic, name='mean_statistic'),

    # ex: /dash/visualization/
    path('visualization/', views.visualization, name='visualization'),

    # ex: /dash/statistics/
    path('statistics/', views.statistics, name='statistics'),
    # ex: /dash/statistics/?metric=consumption&data=neighborhood

    # ex: /dash/comparisons/
    path('comparisons/', views.comparisons, name='comparisons'),
    # ex: /dash/comparisons/?data=neighborhood
    re_path(r'^number_of_comparison/$', views.number_of_comparison),
]
