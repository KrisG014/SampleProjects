from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django import forms
from django.views import generic
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime

from .models import URLEntry
from .mixins import *

# Create your views here.
def index(request):
    return HttpResponse("Hey!  You've logged in!")  

def UserHomeRedirect(request):
    if request.user.username == "":
        return HttpResponseRedirect("/")
    return HttpResponseRedirect(reverse('URLShortener:userurls', kwargs={'pk': request.user.username} ))
    
def UserList(request):
    users = User.objects.all()
    return render(request, 'URLShortener/user_list.html', {'users': users})

def UserURLDetail(request, pk):
    if IsUserLoggedIn(request, pk):
        if request.user.is_authenticated:
            user = get_object_or_404(User, username=pk)
            return render(request, 'URLShortener/user_detail.html', {'user': user})
    elif request.user.username == "":
        return HttpResponseRedirect("/")
    return HttpResponseRedirect(reverse('URLShortener:userurls', kwargs={'pk': request.user.username} ))


class URLCreateView(LoginRequiredMixin, CreateView):
    fields = ("username", "original_url", "shortened_url", "created_date")
    model = URLEntry

    def get_initial(self):
        initial = super(URLCreateView, self).get_initial()
        now = datetime.now()
        initial["username"] = self.request.user
        initial["created_date"] = now.strftime('%Y-%m-%d %H:%M')
        return initial

class URLUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("original_url", "shortened_url", "created_date")
    model = URLEntry


class URLDeleteView(LoginRequiredMixin, DeleteView):
    model = URLEntry
    success_url = reverse_lazy("URLShortener:userurls")

def IsUserLoggedIn(request, username):
    return request.user.username == username

