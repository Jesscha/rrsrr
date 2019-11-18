from django import forms
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'pub_date': forms.TextInput(attrs=
                                        {
                                            'class':'datepicker'
                                        }),
        }
class RawPostModelForm(forms.Form):
    title = forms.CharField()
    pup_date = forms.DateTimeField()
    text = forms.CharField()
    image = forms.FileField(required=False)


