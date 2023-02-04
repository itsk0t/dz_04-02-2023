from django.shortcuts import render
from .models import Imprisoned
from django.views.generic import DetailView

# Create your views here.

def index(request):
    imprisoned = Imprisoned.objects.order_by('-time_start')
    return render(request, 'main/index.html', {'imprisoned': imprisoned})

class ImprisonedView(DetailView):
    model = Imprisoned
    templates_name = 'main/imprisoned_view.html'
    context_object_name = 'imprisoned_post'