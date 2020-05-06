from django import forms
from .models import Activity

class AddForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mr-sm-2',
        'placeholder': 'Enter activity' 
        }), label='')

    class Meta:
        model = Activity
        fields = ['title']
        
class EditForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control mr-sm-2',
        'placeholder': 'Enter activity' 
        }), label='')

    class Meta:
        model = Activity
        fields = ['title']
    