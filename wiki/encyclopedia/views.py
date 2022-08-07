from urllib import request
from django.shortcuts import render, redirect
from django.http import Http404
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    if entry not in util.list_entries():
        raise Http404
    content = util.get_entry(entry)
    return render(request, "encyclopedia/wiki.html",
        {"title": entry, "content": Markdown().content(content)}
    )
    