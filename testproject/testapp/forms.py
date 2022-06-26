from django import forms


class MasterForm(forms.Form):
    masterstr = forms.CharField(max_length=250)

    str1 = forms.CharField(max_length=250)
    str2 = forms.CharField(max_length=250)
    str3 = forms.CharField(max_length=250)
    str4 = forms.CharField(max_length=250)

