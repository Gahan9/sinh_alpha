from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic import TemplateView
from django_tables2 import MultiTableMixin
from django_tables2 import RequestConfig
from django_tables2 import SingleTableMixin
from django_tables2 import SingleTableView

from .models import *
from .forms import *


@login_required(login_url="login/")
def home(request):
    """Rendering home page"""
    return render(request, "home.html")


class InputPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = InputTable
    template_name = 'table_show.html'
    tables = [InputTable(Input.objects.all())]
    table_pagination = {
        'per_page': 15
    }


class AuthPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = AuthTable
    template_name = 'table_show.html'
    tables = [AuthTable(Auth.objects.all())]
    table_pagination = {
        'per_page': 15
    }


class ClientPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = Clients
    template_name = 'table_show.html'
    tables = [ClientsTable(Clients.objects.all())]
    table_pagination = {
        'per_page': 15
    }


class DownloadsPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = Downloads
    template_name = 'table_show.html'
    tables = [DownloadsTable(Downloads.objects.all())]
    table_pagination = {
        'per_page': 15
    }


class SessionPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = Sessions
    template_name = 'table_show.html'
    tables = [SessionsTable(Sessions.objects.all())]
    table_pagination = {
        'per_page': 15
    }


class SensorPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = Sensors
    template_name = 'table_show.html'
    tables = [SensorsTable(Sensors.objects.all())]
    table_pagination = {
        'per_page': 15
    }
