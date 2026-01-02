from django.shortcuts import render


def index(request):
    context = {"var": "Hallo"}
    return render(request, "main/main.html", context)