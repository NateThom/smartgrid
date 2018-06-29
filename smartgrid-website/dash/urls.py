from django.urls import path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.index, name='index'),

    # ex: /dash/visualization/
    path('visualization/', views.visualization, name='visualization'),

    # ex: /dash/statistics/
    path('statistics/', views.statistics, name='statistics'),

    # ex: /dash/comparisons/
    path('comparisons/', views.comparisons, name='comparisons'),
]
