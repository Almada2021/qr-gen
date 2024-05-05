from django.shortcuts import render
from django.http import HttpResponse
from .models import Qr
# Create your views here.
def qrlist(request):
    qrs = Qr.objects.all().order_by('-date')
    return render(request, 'qr/qr_list.html', {'qrs': qrs})

def qr_page(request, slug):
    qr = Qr.objects.get(slug=slug)
    return render(request, 'qr/qr_page.html', {'qr': qr})