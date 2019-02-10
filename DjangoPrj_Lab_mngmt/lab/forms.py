from django import forms
from .models import ClassicalBTS, Asik, Abil, Gps

class AsikForm(forms.ModelForm):
    class Meta:
        model = Asik
        fields = tuple([x.name for x in Asik._meta.fields])
        # fields = ("gps_id",)

class GpsForm(forms.ModelForm):
    class Meta:
        model = Gps
        fields = tuple([x.name for x in Gps._meta.fields])