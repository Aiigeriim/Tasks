from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils import timezone

from webapp.models import status_choices, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # exclude = ('completion_date', 'published_at')
        fields = ('name', 'description', 'status', 'completion_date', 'published_at')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(
                attrs={"cols": "25", "rows": "5", "class": "form-control"}),
            'status': widgets.Select(choices=status_choices,
                 attrs={'class': 'form-control'}),
            'published_at':  widgets.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'completion_date': widgets.DateInput(
                attrs={'type': 'date','class': 'form-control'})
        }
        error_messages = {'title': {"required": "Пожалуйста, введите название"}}

    def clean_published_at(self):
        published_at = self.cleaned_data['published_at']
        if published_at < timezone.now():
            raise ValidationError("This date is in the future")
        return published_at

    def clean(self):
        name = self.cleaned_data.get('name')
        description = self.cleaned_data.get('description')
        if name and description and  name == description:
            raise ValidationError("Название и описание не могут быть одинаковыми")
        return super(TaskForm, self).clean()