from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
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
    template_name = 'input_page.html'
    tables = [InputTable(Input.objects.all())]
    table_pagination = {
        'per_page': 15
    }


def sortedRequest(request):
    """ handle ajax request for sorting """
    if request.is_ajax():
        field_to_sort = request.GET.get('field')
        sortedResponse = Auth.objects.all().order_by('-'+field_to_sort)
        return JsonResponse(sortedResponse)
    else:
        JsonResponse("Error!")


@login_required(login_url="login/")
def auth_page(request):

    auth_data = Auth.objects.all().order_by('-timestamp')
    template = "auth_page.html"
    context = {"auth_data": auth_data}
    return render(request, template, context)


@login_required(login_url="login/")
def client_page(request):
    client_data = Clients.objects.all()
    template = "client_page.html"
    context = {"client_data": client_data}
    return render(request, template, context)


@login_required(login_url="login/")
def downloads_page(request):
    downloads_data = Downloads.objects.all()
    template = "downloads_page.html"
    context = {"downloads_data": downloads_data}
    return render(request, template, context)


@login_required(login_url="login/")
def session_page(request):
    session_data = Sessions.objects.all()
    template = "session_page.html"
    context = {"session_data": session_data}
    return render(request, template, context)


@login_required(login_url="login/")
def sensor_page(request):
    sensor_data = Sensors.objects.all()
    template = "sensor_page.html"
    context = {"sensor_data": sensor_data}
    return render(request, template, context)


def search_auth(request):
    """ Implemented to sniff entries in database """
    auth_filter = {"session": request.GET.get('session', None),
          "success": request.GET.get('success', None),
          "username": request.GET.get('username', None),
          "password": request.GET.get('password', None),
           "timestamp": request.GET.get('timestamp', None),
           "ip": request.GET.get('ip', None)
          }

    req_data = dict(filter(lambda x: x[1], auth_filter.items()))

    id_ = request.GET.get('id', None)

    if req_data:
        refined_search = Auth.objects.filter(**req_data)
        return render(request, 'results.html', {'refined_search': refined_search}, {'query': id_})
    else:
        error = 'No match found'
        return HttpResponse(error)
