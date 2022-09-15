from django import forms
from .models import clothe

class clotheForm(forms.ModelForm):
    name = forms.CharField(max_length=20)
    parent_category = forms.CharField(max_length=20)
    child_category = forms.CharField(max_length=20)
    season = forms.CharField(max_length=20)
    style = forms.CharField(max_length=20)
    color = forms.CharField(max_length=20)
    memo = forms.CharField(max_length=20)



    class Meta:
        model = clothe
        fields = ("name", "parent_category",'child_category', "season", "style", "color","memo")