from django.http import HttpResponse
from django.shortcuts import render
from Entries.models import EntryV1

# Create your views here.

def book_start(request) -> HttpResponse:
    context = {"var": "Hallo"}
    return render(request, "book_explorer/book.html", context)

def next_entry(request, source_id: int) -> HttpResponse:
    context = {
        "current_entry": EntryV1.objects.filter(pk=source_id + 1).first(),
        "previous_entry": EntryV1.objects.filter(pk=source_id).first(),
               }
    print(context)
    return render(request, "book_explorer/animated_entry.html", context)


def previous_entry(request, source_id: int) -> HttpResponse:
    context = {
        "current_entry": EntryV1.objects.filter(pk=source_id).first(),
        "previous_entry": EntryV1.objects.filter(pk=source_id - 1).first(),
        "transition" : "prev"
    }
    return render(request, "book_explorer/animated_entry.html", context)