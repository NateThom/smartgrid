from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.dash, name='dash'),
    # ex: /dash/dash_statistics_mean_1/
    path('dash_statistics_mean_1/', views.dash_statistics_mean_1, name='dash_statistics_mean_1'),
    # ex: /dash/statistics_mean_2?position_field=Region&measurement_field=Consumption&modifier_field=Exact+Temperature&year_choices=dJaE&time_period_field=Year
    re_path(r'^dash_statistics_mean_1/dash_statistics_mean_2/$', views.dash_statistics_mean_2, name='dash_statistics_mean_2'),
    # ex: /dash/dash_statistics_mean_1/dash_statistics_mean_2/dash_statistics_mean_solution/?position_field=1&modifier_field=z&time_period_field=cSqa
    re_path(r'^dash_statistics_mean_1/dash_statistics_mean_2/dash_statistics_mean_solution/$', views.dash_statistics_mean_solution, name='dash_statistics_mean_solution'),
    # ex: /dash/mean_statistic/?metric=consumption&data=neighborhood
    re_path(r'^mean_statistic/$', views.mean_statistic, name='mean_statistic'),
]
