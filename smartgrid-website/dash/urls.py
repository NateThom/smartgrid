from django.urls import path, re_path

from . import views

app_name = 'dash'
urlpatterns = [
    # ex: /dash/
    path('', views.index, name='index'),
]
