from django.shortcuts import render

# Create your views here.
def qrlist(request):
    return render(request, 'qr/qr_list.html')