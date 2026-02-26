from django.shortcuts import render
from .models import SliderImage


def home(request):
    slides = SliderImage.objects.filter(is_active=True).order_by("order")
    return render(request, "home.html", {"slides": slides})