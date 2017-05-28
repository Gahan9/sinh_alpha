from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.detail import SingleObjectMixin

from django_tables2 import MultiTableMixin
from django_tables2 import RequestConfig
from django_tables2 import SingleTableMixin
from django_tables2 import SingleTableView

from chartit import DataPool, Chart
from django.db.models import Avg
from chartit import PivotDataPool, PivotChart
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
    tables = [InputTable(Input.objects.all().order_by('-timestamp'))]
    table_pagination = {
        'per_page': 20
    }


class AuthPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = AuthTable
    template_name = 'table_show.html'
    tables = [AuthTable(Auth.objects.all().order_by('-timestamp'))]
    table_pagination = {
        'per_page': 15
    }

    # def get_context_data(self, **kwargs):
    #     kwargs['form'] = self.get_form()
    #     context = {'ip': 'Add New Book'}
    #     context.update(kwargs)
    #     return super(SingleObjectMixin, self).get_context_data(**context)


def breach_attempt_chart_view(request):
    breach_attempt_data = PivotDataPool(series=[{'options': {'source': Auth.objects.filter(username='project'),
                                                 'categories': ['success'],
                                                 'legend_by': 'username',
                                                 'top_n_per_cat': 3,
                                                 },
                                                'terms': {'avg_breach': Avg('success')}}])

    chart_obj = PivotChart(datasource=breach_attempt_data,
                      series_options=[{'options': {'type': 'column', 'stacking': True},
                                       'terms': ['avg_breach']}],
                      chart_options={'title': {'text': 'Breach Report'},
                                     'xAxis': {'title': {'text': 'x--------axis'}}})
    return render(request, 'chart_represent.html', {'chart_object': chart_obj})


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
    tables = [DownloadsTable(Downloads.objects.all().order_by('-timestamp'))]
    table_pagination = {
        'per_page': 15
    }


class SessionPageView(LoginRequiredMixin, MultiTableMixin, TemplateView):
    """ Show all input commands entered by attacker """
    login_url = reverse_lazy('login')
    table_class = Sessions
    template_name = 'table_show.html'
    tables = [SessionsTable(Sessions.objects.all().order_by('-starttime'))]
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
