from django.shortcuts import render
from .utils import hitung_wp


# Create your views here.
def hasil_wp(request):
    ranking = hitung_wp()
    return render(request, "staff_selector/hasil_wp.html", {"ranking": ranking})
