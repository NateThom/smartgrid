from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.dash, name='dash'),
    # ex: /dash/dash_load_data1/
    path('dash_load_data1/', views.dash_load_data1, name='dash_load_data1'),
    # ex: /dash/dash_load_data1/dash_load_data2/?file_path=%7E%2FDownloads%2Fpower_consumption.txt
    re_path('dash_load_data1/dash_load_data2/$', views.dash_load_data2, name='dash_load_data2'),
    # ex: /dash/dash_statistics_mean_1/
    path('dash_statistics_mean_1/', views.dash_statistics_mean_1, name='dash_statistics_mean_1'),
    # ex: /dash/statistics_mean_2?position_field=Region&measurement_field=Consumption&modifier_field=Exact+Temperature&year_choices=dJaE&time_period_field=Year
    re_path(r'^dash_statistics_mean_1/dash_statistics_mean_2/$', views.dash_statistics_mean_2, name='dash_statistics_mean_2'),
    # ex: /dash/dash_statistics_mean_1/dash_statistics_mean_2/dash_statistics_mean_solution/?position_field=1&modifier_field=z&time_period_field=cSqa
    re_path(r'^dash_statistics_mean_1/dash_statistics_mean_2/dash_statistics_mean_solution/$', views.dash_statistics_mean_solution, name='dash_statistics_mean_solution'),
]
