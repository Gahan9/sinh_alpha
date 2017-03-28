from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404, request, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Auth, Input, Clients, Downloads, Sensors, Sessions
from .forms import ChangePassword


@login_required(login_url="login/")
def home(request):
    """Rendering home page"""
    return render(request, "home.html")


@login_required(login_url="login/")
def change_password(request):
    if request.method == 'POST':
        current_user = request.user.username
        reset_form = ChangePassword(request.POST, user=request.user)
        if reset_form.is_valid():
            u = User.objects.get(username__exact=current_user)
            u.set_password(reset_form.cleaned_data['password2'])
            u.save()
            return HttpResponseRedirect('/')
    else:
        reset_form = ChangePassword(user=request.user.username)
    return render(request, 'change_password.html', {'reset_form': reset_form})


@login_required(login_url="login/")
def input_page(request):
    """show input table"""
    input_data = Input.objects.all().order_by('id')
    # template = "input_page.html"
    # context = {"input_data" : input_data}
    # return render(request , template, context)
    return render(request, "input_page.html", {"input_data": input_data})


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
