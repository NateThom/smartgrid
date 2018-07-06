from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.index, name='index'),

    # ex: /dash/visualization/
    path('visualization/', views.visualization, name='visualization'),

    # ex: /dash/statistics/
    path('statistics/', views.statistics, name='statistics'),
    # ex: /dash/statistics/?metric=consumption&data=neighborhood
    re_path(r'^mean_statistic/$', views.mean_statistic),

    # ex: /dash/comparisons/
    path('comparisons/', views.comparisons, name='comparisons'),
    # ex: /dash/comparisons/?data=neighborhood
    re_path(r'^number_of_comparison/$', views.number_of_comparison),
]
