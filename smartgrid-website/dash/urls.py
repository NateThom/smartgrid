from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.dash, name='dash'),
    # ex: /dash/dash_create_data_1/
    path('dash_create_data_1/', views.dash_create_data_1, name='dash_create_data_1'),
    # ex: /dash/dash_create_data_1/dash_create_data_2/?data_options_field=Region&data_options_field=Aggregator&data_options_field=Neighborhood
    re_path('dash_create_data_1/dash_create_data_2/$', views.dash_create_data_2, name='dash_create_data_2'),
    # ex: http://127.0.0.1:8000/dash/dash_create_data_1/dash_create_data_2/dash_create_data_3/?number_of_regions_field=1
    # &number_of_aggregators_field=1&number_of_neighborhoods_field=1&number_of_houses_field=1&number_of_readings_field=1
    # &start_year=1&end_year=1&max_consumption=1&consumption_units=kWh&min_temperature=0&max_temperature=0&temperature_units=F&currency_of_cost=USD
    re_path('dash_create_data_1/dash_create_data_2/dash_create_data_3/$', views.dash_create_data_3, name='dash_create_data_3'),
    # ex: /dash/dash_load_data_1/
    path('dash_load_data_1/', views.dash_load_data_1, name='dash_load_data_1'),
    # ex: /dash/dash_load_data_1/dash_load_data_2/?file_path=%7E%2FDownloads%2Fpower_consumption.txt
    re_path('dash_load_data_1/dash_load_data_2/$', views.dash_load_data_2, name='dash_load_data_2'),
    # ex: /dash/dash_statistics_1/
    path('dash_statistics_1/', views.dash_statistics_1, name='dash_statistics_1'),
    # ex: /dash/statistics_2?position_field=Region&measurement_field=Consumption&modifier_field=Exact+Temperature&year_choices=dJaE&time_period_field=Year
    re_path(r'^dash_statistics_1/dash_statistics_2/$', views.dash_statistics_2, name='dash_statistics_2'),
    # ex: /dash/dash_statistics_1/dash_statistics_2/dash_statistics_solution/?position_field=1&modifier_field=z&time_period_field=cSqa
    re_path(r'^dash_statistics_1/dash_statistics_2/dash_statistics_solution/$', views.dash_statistics_solution, name='dash_statistics_solution'),
]
