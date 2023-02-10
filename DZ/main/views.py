from django.shortcuts import render
from .models import Imprisoned
from django.views.generic import DetailView
from .forms import ImprisonedForm
# Create your views here.

def index(request):
    imprisoned = Imprisoned.objects.order_by('-time_start')
    return render(request, 'main/index.html', {'imprisoned': imprisoned})

class ImprisonedView(DetailView):
    model = Imprisoned
    template_name = 'main/imprisoned_view.html'
    context_object_name = 'imprisoned_post'

def create(request):
    form = ImprisonedForm()

    data = {
        'form': form
    }

    return render(request, 'main/imprisoned_create.html')