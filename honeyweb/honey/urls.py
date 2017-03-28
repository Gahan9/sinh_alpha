from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^password_change', views.change_password, name="password_change"),
    url(r'^input$', views.input_page, name='input_page'),
    url(r'^auth$', views.auth_page, name='auth_page'),
    url(r'^client$', views.client_page, name='client_page'),
    url(r'^downloads$', views.downloads_page, name='downloads_page'),
    url(r'^session$', views.session_page, name='session_page'),
    url(r'^sensor$', views.sensor_page, name='sensor_page'),
]
