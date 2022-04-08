from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from markdown2 import Markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_md = util.get_entry(title)
    if entry_md == None:
        return render(request, "encyclopedia/error.html", {"message": "Page not found."})
    else:
        entry_html = Markdown().convert(entry_md)
        context = {
            "tilte": title,
            "entry": entry_html
        }
        return render(request, "encyclopedia/entry.html", context)

def search(request):
    return HttpResponseRedirect(reverse("index"))
    # return render(request, "encyclopedia/search.html", context)