from django import forms
from info.models import Resource, ContactUsResponse

class ResourceForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    class Meta:
        model = Resource
        fields = ['title', 'categories', 'url', 'brief', 'detail']
        labels = {
            'title': 'Title *',
            'categories': 'Categories (Multiple) *',
            'url': 'URL',
            'brief': 'Brief *',
            'detail': 'Detail (Markdown for Styling) *',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':True}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control', 'required':True, }),
            'url': forms.TextInput(attrs={'class': 'form-control',}),
            'brief': forms.TextInput(attrs={'class': 'form-control', 'required':True, }),
            'detail': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUsResponse
        fields = ['name', 'organization', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required':True, 'placeholder': 'Your Name'}),
            'organization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Organization'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required':True, 'placeholder': 'Your Email' }),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': False, 'placeholder': 'Your Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'required': False, 'placeholder': 'Your Message for Us'}),
        }
