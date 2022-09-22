from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_index(request):
    return render(request, "index_mywatchlist.html")

def show_mywatchlist(request):
    return render(request, "mywatchlist.html", context)

context = {
    'list_film': MyWatchList.objects.all(),
    'name': 'Ferry',
    'student_id': '2106701936'
}

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")