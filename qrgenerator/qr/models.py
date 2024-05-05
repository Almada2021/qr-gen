from typing import Any
from django.db import models

# Create your models here.
class Qr (models.Model):
    title  = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='fallback.png', blank=True)
    # los metodos no cambian el modelo no necesario migrar
    def __str__(self) -> str:
        return self.title