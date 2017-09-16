from django import forms

from .models import attsheet

class attform(forms.ModelForm):
    from_date=forms.DateField(widget=forms.SelectDateWidget)
    to_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model=attsheet
        fields=['name','contact_no','room_no','from_date','to_date','purpose']







