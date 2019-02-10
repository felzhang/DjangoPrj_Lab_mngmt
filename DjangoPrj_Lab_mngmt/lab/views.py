# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import ClassicalBTS, Asik, Abil, Gps
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
#
# def lab_asik_detail(request, asik_id):
#     asik = get_object_or_404(Asik, id=asik_id)
#     return render(request, "lab/asik_detail.html", {"asik":asik})

def lab_asik_detail_form(request, asik_id):
    asik_initial = Asik.objects.filter(id = asik_id).values()[0]
    print(asik_initial)
    form = AsikForm(initial=asik_initial)
    # form = AsikForm(initial={'gps_id':'2'})

    if request.method == "POST":
        form = AsikForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            Asik.objects.filter(id=asik_id).update(**data)
        else:
            print("data is not valid")
    return render(request, "lab/asik_detail_form.html", {"asik_form":form, "asik_id":asik_id})

def lab_asik_delete(request, asik_id):
    asik = get_object_or_404(Asik, id=asik_id)
    asik.delete()
    return HttpResponseRedirect(reverse("lab:asik"))

def lab_asik_add(request):
    asik_form = AsikForm()
    if request.method == "POST":
        asik_form = AsikForm(request.POST)
        if asik_form.is_valid():
            data = asik_form.cleaned_data
            asik_form.save()
            return HttpResponseRedirect(reverse("lab:asik"))
    return render(request, "lab/asik_detail_form.html", {"asik_form":asik_form})
