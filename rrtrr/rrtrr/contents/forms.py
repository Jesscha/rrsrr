from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'pub_date',
            'text',
            'image'
        ]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['title'].widget.attrs.update({'class': 'special'})
            self.fields['pup_date'].widget.attrs.update(size='40')

class RawPostModelForm(forms.Form):
    title = forms.CharField()
    pup_date = forms.DateTimeField()
    text = forms.CharField()
    image = forms.FileField(required=False)


