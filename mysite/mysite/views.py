from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        if request.user.username != "":
            return HttpResponseRedirect(reverse('URLShortener:userurls', kwargs={'pk': request.user.username}))
        return render(request, 'index.html')

def about(request):
    user_has_id = False
    if request.user.username != "":
        user_has_id = True
    return render(request, 'about.html', {'user_has_id': user_has_id})

def ShortenedURLRedirect(request, user_id, pk):
    return HttpResponseRedirect(reverse('URLShortener:url_redirect', kwargs={'user_id' : user_id, 'pk': pk}))
