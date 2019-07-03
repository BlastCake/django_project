from django.shortcuts import render, get_object_or_404
from .models import *

class ObjectDetailMixin:
    # Создали этот класс так как во .views.py в классах PostDetail и TagDetail пратически идентичные методы get
    model = None
    template = None
    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})