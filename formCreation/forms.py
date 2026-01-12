from django import forms

class InuputForm(forms.Form):
    firstName = forms.CharField(max_length = 200)
    lastName = forms.CharField(max_length=200)
    MobileNo = forms.IntegerField(help_text="Enter 9 digit no")
    Password = forms.CharField(widget=forms.PasswordInput())
