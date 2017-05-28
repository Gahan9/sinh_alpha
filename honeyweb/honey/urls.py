from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^report$', views.breach_attempt_chart_view, name='breach_attempt_chart_view'),
    url(r'^input$', views.InputPageView.as_view(), name='input_page'),
    url(r'^auth$', views.AuthPageView.as_view(), name='auth_page'),
    url(r'^client$', views.ClientPageView.as_view(), name='client_page'),
    url(r'^downloads$', views.DownloadsPageView.as_view(), name='downloads_page'),
    url(r'^session$', views.SessionPageView.as_view(), name='session_page'),
    url(r'^sensor$', views.SensorPageView.as_view(), name='sensor_page'),
]
