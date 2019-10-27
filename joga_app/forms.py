from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Name:', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.EmailField(label='Email:', max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
