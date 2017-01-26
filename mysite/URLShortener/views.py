from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy
from django import forms
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import User, URLEntry

# Create your views here.
def index(request):
    return HttpResponse("Hey!  You've logged in!")  

def login(request, template_name='templates/URLShortener/registration/login.html'):
    HttpResponseRedirect('URLShortener/index.html')
    
def UserList(request):
    users = User.objects.all()
    return render(request, 'URLShortener/user_list.html', {'users': users})

def UserURLDetail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'URLShortener/user_urls.html', {'user': user})

class UserDetailView(DetailView):
    model = User

class UserCreateView(CreateView):
    fields = ("username", "first_name", "last_name", "email", "password")
    model = User

class URLCreateView(CreateView):
    fields = ("username", "original_url", "shortened_url", "created_date")
    model = URLEntry

class UserUpdateView(UpdateView):
    fields = ("username", "first_name", "last_name", "email", "password")
    model = User

class URLUpdateView(UpdateView):
    fields = ("original_url", "shortened_url", "created_date")
    model = URLEntry

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("home")

class URLDeleteView(DeleteView):
    model = URLEntry
    success_url = reverse_lazy("userurls")