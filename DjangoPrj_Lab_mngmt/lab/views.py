# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import ClassicalBTS, Asik, Abil, Gps, Rru, Amia, Pb
from .forms import AsikForm, GpsForm, ClassicalBTSForm, AbilForm, RruForm, AmiaForm, PbForm

# Create your views here.
# classicalbts view functions
def lab_classicalbts(request):
    classicalbtss = ClassicalBTS.objects.all()
    return render(request, "lab/classicalbtss.html", {"classicalbtss":classicalbtss})

def lab_classicalbts_detail_form(request, classicalbts_id):
    classicalbts_initial = get_object_or_404(ClassicalBTS, id=classicalbts_id)
    form = ClassicalBTSForm(request.POST or None, instance=classicalbts_initial)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("lab:classicalbts"))
    return render(request, "lab/classicalbts_detail_form.html", {"classicalbts_form": form, "classicalbts_id": classicalbts_id})

def lab_classicalbts_delete(request, classicalbts_id):
    classicalbts = get_object_or_404(ClassicalBTS, id=classicalbts_id)
    classicalbts.delete()
    return HttpResponseRedirect(reverse("lab:classicalbts"))

def lab_classicalbts_add(request):
    classicalbts_form = ClassicalBTSForm()
    if request.method == "POST":
        classicalbts_form = ClassicalBTSForm(request.POST)
        if classicalbts_form.is_valid():
            classicalbts_form.save()
            return HttpResponseRedirect(reverse("lab:classicalbts"))
    return render(request, "lab/classicalbts_detail_form.html", {"classicalbts_form":classicalbts_form})


# asik view functions
def lab_asik(request):
    asiks = Asik.objects.all()
    return render(request, "lab/asiks.html", {"asiks":asiks})

def lab_asik_detail_form(request, asik_id):

    # 在 form = AsikFrom()定义时， 有两个参数，
    # initail  -- 如定义此参数，表明新数据插入到AsikForm对应的model中，新增数据
    # instance  -- 如定义此参数，不插入新数据，而是更新此model中到已有数据（通过id定位到数据）
    # 此函数是为了更新asik_id的数据，不是插入新数据，所以不用initail，而是instance
    # 错误： asik_initial = Asik.objects.filter(id = asik_id).values()[0]    form = AsikForm(initial=asik_initial)
    # 正确： asik_initial = get_object_or_404(Asik, id=asik_id)    form = AsikForm(request.POST or None, instance=asik_initial)
    asik_initial = get_object_or_404(Asik, id=asik_id)
    form = AsikForm(request.POST or None, instance=asik_initial)
    if form.is_valid():    # .is_valid做了很多事情，如果此步不通过，.cleaned_data会没有定义
        form.save()
        return HttpResponseRedirect(reverse("lab:asik"))
    return render(request, "lab/asik_detail_form.html", {"asik_form": form, "asik_id": asik_id})

def lab_asik_delete(request, asik_id):
    asik = get_object_or_404(Asik, id=asik_id)
    asik.delete()
    return HttpResponseRedirect(reverse("lab:asik"))

def lab_asik_add(request):
    asik_form = AsikForm()    # 未传入instance参数，则表明新增数据，插入model中。
    if request.method == "POST":
        asik_form = AsikForm(request.POST)
        if asik_form.is_valid():
            asik_form.save()
            return HttpResponseRedirect(reverse("lab:asik"))
    return render(request, "lab/asik_detail_form.html", {"asik_form":asik_form})


def lab_abil(request):
    abils = Abil.objects.all()
    return render(request, "lab/abils.html", {"abils":abils})

# gps view functions
def lab_gps(request):
    gpss = Gps.objects.all()
    return render(request, "lab/gpss.html", {"gpss": gpss})

def lab_gps_detail_form(request, gps_id):
    gps_instance = get_object_or_404(Gps, id=gps_id)
    form = GpsForm(request.POST or None, instance=gps_instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("lab:gps"))
    return render(request, "lab/gps_detail_form.html", {"gps_form": form, "gps_id": gps_id})

def lab_gps_delete(request, gps_id):
    gps = get_object_or_404(Gps, id=gps_id)
    gps.delete()
    return HttpResponseRedirect(reverse("lab:gps"))

def lab_gps_add(request):
    gps_form = GpsForm()
    if request.method == "POST":
        gps_form = GpsForm(request.POST)
        if gps_form.is_valid():
            gps_form.save()
            return HttpResponseRedirect(reverse("lab:gps"))
    return render(request, "lab/gps_detail_form.html", {"gps_form":gps_form})

# abil view functions
def lab_abil(request):
    abils = Abil.objects.all()
    return render(request, "lab/abils.html", {"abils": abils})

def lab_abil_detail_form(request, abil_id):
    abil_instance = get_object_or_404(Abil, id=abil_id)
    form = AbilForm(request.POST or None, instance=abil_instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("lab:abil"))
    return render(request, "lab/abil_detail_form.html", {"abil_form": form, "abil_id": abil_id})

def lab_abil_delete(request, abil_id):
    abil = get_object_or_404(Abil, id=abil_id)
    abil.delete()
    return HttpResponseRedirect(reverse("lab:abil"))

def lab_abil_add(request):
    abil_form = AbilForm()
    if request.method == "POST":
        abil_form = AbilForm(request.POST)
        if abil_form.is_valid():
            abil_form.save()
            return HttpResponseRedirect(reverse("lab:abil"))
    return render(request, "lab/abil_detail_form.html", {"abil_form":abil_form})

# rru view functions
def lab_rru(request):
    rrus = Rru.objects.all()
    return render(request, "lab/rrus.html", {"rrus": rrus})

def lab_rru_detail_form(request, rru_id):
    rru_instance = get_object_or_404(Rru, id=rru_id)
    form = RruForm(request.POST or None, instance=rru_instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("lab:rru"))
    return render(request, "lab/rru_detail_form.html", {"rru_form": form, "rru_id": rru_id})

def lab_rru_delete(request, rru_id):
    rru = get_object_or_404(Rru, id=rru_id)
    rru.delete()
    return HttpResponseRedirect(reverse("lab:rru"))

def lab_rru_add(request):
    rru_form = RruForm()
    if request.method == "POST":
        rru_form = RruForm(request.POST)
        if rru_form.is_valid():
            rru_form.save()
            return HttpResponseRedirect(reverse("lab:rru"))
    return render(request, "lab/rru_detail_form.html", {"rru_form":rru_form})

# amia view functions
def lab_amia(request):
    amias = Amia.objects.all()
    return render(request, "lab/amias.html", {"amias": amias})

def lab_amia_detail_form(request, amia_id):
    amia_instance = get_object_or_404(Amia, id=amia_id)
    form = AmiaForm(request.POST or None, instance=amia_instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("lab:amia"))
    return render(request, "lab/amia_detail_form.html", {"amia_form": form, "amia_id": amia_id})

def lab_amia_delete(request, amia_id):
    amia = get_object_or_404(Amia, id=amia_id)
    amia.delete()
    return HttpResponseRedirect(reverse("lab:amia"))

def lab_amia_add(request):
    amia_form = AmiaForm()
    if request.method == "POST":
        amia_form = AmiaForm(request.POST)
        if amia_form.is_valid():
            amia_form.save()
            return HttpResponseRedirect(reverse("lab:amia"))
    return render(request, "lab/amia_detail_form.html", {"amia_form":amia_form})

# pb view functions
def lab_pb(request):
    pbs = Pb.objects.all()
    return render(request, "lab/pbs.html", {"pbs": pbs})

def lab_pb_detail_form(request, pb_id):
    pb_instance = get_object_or_404(Pb, id=pb_id)
    form = PbForm(request.POST or None, instance=pb_instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("lab:pb"))
    return render(request, "lab/pb_detail_form.html", {"pb_form": form, "pb_id": pb_id})

def lab_pb_delete(request, pb_id):
    pb = get_object_or_404(Pb, id=pb_id)
    pb.delete()
    return HttpResponseRedirect(reverse("lab:pb"))

def lab_pb_add(request):
    pb_form = PbForm()
    if request.method == "POST":
        pb_form = PbForm(request.POST)
        if pb_form.is_valid():
            pb_form.save()
            return HttpResponseRedirect(reverse("lab:pb"))
    return render(request, "lab/pb_detail_form.html", {"pb_form":pb_form})