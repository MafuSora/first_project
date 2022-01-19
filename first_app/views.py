from django.shortcuts import render
from . import op_hitung
# Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    return render(request, 'var_desain.html', {'bil1': op_hitung.a, 'bil2': op_hitung.b, 'jumlah': op_hitung.tambah, 'kurang': op_hitung.kurang, 'kali': op_hitung.kali, 'bagi': op_hitung.bagi, 'sisa_bagi': op_hitung.sisa_bagi})


def applist(request):
    return render(request, 'list_desain.html', {'bil1': op_hitung.a, 'bil2': op_hitung.b, 'hasil': op_hitung.hasil})
