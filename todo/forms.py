from django.forms import ModelForm
from .models import Todo
from django import forms


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'memo', 'importance')
        widgets = {
            'memo': forms.Textarea(attrs={'rows': 4, 'cols': 38}),
            'title': forms.Textarea(attrs={'rows': 1, 'cols': 38})
        }
