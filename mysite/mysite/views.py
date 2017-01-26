from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View, TemplateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)
        context["users"] = ['kgalane', 'dcarrick']
        return context
