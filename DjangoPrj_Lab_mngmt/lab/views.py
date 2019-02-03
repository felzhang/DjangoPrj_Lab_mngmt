# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import ClassicalBTS, Asik, Abil
from .forms import AsikForm

# Create your views here.
def lab_classicalbts(request):
    classicalbtss = ClassicalBTS.objects.all()
    return render(request, "lab/classicalbtss.html", {"classicalbtss":classicalbtss})

def lab_asik(request):
    asiks = Asik.objects.all()
    return render(request, "lab/asiks.html", {"asiks":asiks})

def lab_abil(request):
    abils = Abil.objects.all()
    return render(request, "lab/abils.html", {"abils":abils})

def lab_asik_detail(request, asik_id):
    asik = get_object_or_404(Asik, id=asik_id)
    return render(request, "lab/asik_detail.html", {"asik":asik})

def lab_asik_detail_form(request, asik_id):
    asik_initial = Asik.objects.filter(id = asik_id).values()[0]
    form = AsikForm(initial=asik_initial)

    if request.method == "POST":
        form =  AsikForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Asik.objects.filter(id=asik_id).update(**data)
    return render(request, "lab/asik_detail_form.html", {"asik_form":form, "asik_id":asik_id})

def lab_asik_delete(request, asik_id):
    asik = get_object_or_404(Asik, id=asik_id)
    asik.delete()
    return HttpResponseRedirect(reverse("lab:ASIK"))