from django.urls import path
from . import views

app_name = "qrs"
urlpatterns = [
    path('', views.qrlist, name='list'),
    path('<slug:slug>', views.qr_page, name='page'),
    path('add/', views.qr_add_view, name='add'),
    path('make/', views.qr_make_view, name='make'),
]
