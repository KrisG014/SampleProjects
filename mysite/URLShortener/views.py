from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from datetime import datetime

from .models import URLEntry
from .mixins import *
from .functions import *

# Create your views here.
def index(request):
    return HttpResponse("Hey!  You've logged in!")  

def UserHomeRedirect(request):
    if request.user.username == "":
        return HttpResponseRedirect("/")
    return HttpResponseRedirect(reverse('URLShortener:userurls', kwargs={'pk': request.user.username} ))

@login_required(login_url='/')
def UserURLDetail(request, pk):
    if IsUserLoggedIn(request, pk):
        if request.user.is_authenticated:
            urls = URLEntry.objects.filter(user=request.user)
            return render(request, 'URLShortener/user_detail.html', {'urls': urls})
    elif request.user.username == "":
        return HttpResponseRedirect("/")
    return HttpResponseRedirect(reverse('URLShortener:userurls', kwargs={'pk': request.user.username} ))

@login_required(login_url='/')
def URLCreateView(request, pk):
    return render(request, "URLShortener/urlcreate_form.html",  {'enter_valid_url': False} )

class URLUpdateView(LoginRequiredMixin, UpdateView):
    fields = ("original_url", "shortened_url", "created_date")
    model = URLEntry


class URLDeleteView(LoginRequiredMixin, DeleteView):
    model = URLEntry
    success_url = reverse_lazy("URLShortener:user_home")

@login_required(login_url='/')
def URLCreationCompleteRedirect(request, pk):
    original_url = request.POST.get('original_url')
    val = URLValidator()
    try:
        val(original_url)
    except ValidationError, e:
        return render(request, "URLShortener/urlcreate_form.html", {'enter_valid_url': True})

    url_id, is_duplicate = UniqueID(original_url, request.user)
    shortened_url = CreateShortenedURL(pk, url_id)
    now = datetime.now()
    created_date = now.strftime('%Y-%m-%d %H:%M')
    url_entry = ""
    if is_duplicate:
        url_entry = URLEntry.objects.get(url_id=url_id,)
    else:
        url_entry = URLEntry.objects.create(url_id=url_id, user=request.user, original_url=original_url, shortened_url=shortened_url, created_date=created_date)
    return render(request, "URLShortener/urlentry_form.html", {'urlentry': url_entry})

def URLRedirect(request, user_id, pk):
    url_entry = get_object_or_404(URLEntry, url_id=pk)
    return HttpResponseRedirect(url_entry.original_url)