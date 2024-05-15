from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required 
from .models import Qr
from .import forms
from django.core.files.base import ContentFile
from io import BytesIO
import qrcode
# Create your views here.
@login_required(login_url="/users/login")
def qrlist(request):
    qrs = Qr.objects.all().order_by('-date')
    return render(request, 'qr/qr_list.html', {'qrs': qrs})

@login_required(login_url="/users/login")
def qr_page(request, slug):
    qr = Qr.objects.get(slug=slug)
    return render(request, 'qr/qr_page.html', {'qr': qr})

@login_required(login_url="/users/login")
def qr_add_view(request: HttpRequest):
    if request.method == "POST":
        form = forms.CreateQr(request.POST, request.FILES)
        if form.is_valid():
            newqr = form.save(commit=False)
            newqr.author = request.user
            newqr.save()
            return redirect('qrs:list')
    else:
        form = forms.CreateQr()
        return render(request, 'qr/qr_add.html', { 'form': form })


@login_required(login_url="/users/login")
def qr_make_view(request):
    if request.method == "POST":
        form = forms.MakeQr(request.POST)
        if form.is_valid():
            newqr = form.save(commit=False)
            newqr.author = request.user
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(form.cleaned_data['url'])
            qr.make(fit=True)

            # Crear la imagen QR y guardarla en un objeto BytesIO
            img = qr.make_image(fill='black', back_color='white')
            temp_handle = BytesIO()
            img.save(temp_handle, format='PNG')
            temp_handle.seek(0)
            # Guardar la imagen en el modelo
            name = f'{form.cleaned_data['title']}{form.cleaned_data['slug']}.png'
            newqr.image.save(name , ContentFile(temp_handle.read()), save=False)
            newqr.save()
            return redirect('qrs:list')
        return render(request, 'qr/qr_make.html')
    else:
        form = forms.MakeQr()
        return render(request, 'qr/qr_make.html', { "form": form})
    