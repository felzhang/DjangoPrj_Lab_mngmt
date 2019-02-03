from django import forms
from .models import ClassicalBTS, Asik, Abil

class AsikForm(forms.ModelForm):
    class Meta:
        model = Asik
        fields = tuple([x.name for x in Asik._meta.fields])