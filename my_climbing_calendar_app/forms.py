from django import forms
from .models import Day, Note

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['date', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['day', 'text']
