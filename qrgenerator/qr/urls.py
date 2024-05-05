from django.urls import path
from . import views

app_name = "qrs"
urlpatterns = [
    path('', views.qrlist, name='list'),
    path('<slug:slug>', views.qr_page, name='page'),
]
