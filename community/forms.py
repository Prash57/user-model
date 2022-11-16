from django.forms import ModelForm
from .models import Feed, Tag
from django import forms

class FeedForm(ModelForm):
    class Meta:
        model = Feed
        fields = ['post', 'tags']

        widgets = {
            'tags': forms.SelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(FeedForm, self).__init__(*args, **kwargs)

