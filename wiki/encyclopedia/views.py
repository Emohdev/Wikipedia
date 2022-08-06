from urllib import request
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def html(request):
    return render(request, "encyclopedia/html.html", {
        "entries/HTML.md": util.list_entries()
    })    

