from django import forms
from .models import ClassicalBTS, Asik, Abil, Gps, Rru, Amia, Pb

class AsikForm(forms.ModelForm):
    class Meta:
        model = Asik
        fields = tuple([x.name for x in Asik._meta.fields])

class GpsForm(forms.ModelForm):
    class Meta:
        model = Gps
        fields = tuple([x.name for x in Gps._meta.fields])
        
class ClassicalBTSForm(forms.ModelForm):
    class Meta:
        model = ClassicalBTS
        fields = tuple([x.name for x in ClassicalBTS._meta.fields])
        
class AbilForm(forms.ModelForm):
    class Meta:
        model = Abil
        fields = tuple([x.name for x in Abil._meta.fields])
        
class RruForm(forms.ModelForm):
    class Meta:
        model = Rru
        fields = tuple([x.name for x in Rru._meta.fields])
        
class AmiaForm(forms.ModelForm):
    class Meta:
        model = Amia
        fields = tuple([x.name for x in Amia._meta.fields])
        
class PbForm(forms.ModelForm):
    class Meta:
        model = Pb
        fields = tuple([x.name for x in Pb._meta.fields])