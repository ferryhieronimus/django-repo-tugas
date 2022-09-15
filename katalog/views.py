from django.shortcuts import render
from katalog.models import CatalogItem

def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'name': 'Ferry',
        'student_id': '2106701936',
        'list_katalog': data_barang_katalog
    }
    return render(request, "katalog.html", context)
