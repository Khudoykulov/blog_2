from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'website', 'message', 'image']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Name...',
            'id': 'name'
        })
        self.fields['website'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'website...',
            'id': "website"
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Message...',
            'cols': "30",
            'rows': "10",
            'id': "message"
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email...',
            'id': 'email'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
