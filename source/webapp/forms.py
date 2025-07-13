from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from webapp.models import Task, TaskType


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for v in self.visible_fields():
            if not isinstance(v.field.widget, widgets.CheckboxSelectMultiple):
                v.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type']
        widgets = {
            'type': forms.CheckboxSelectMultiple()
        }
        error_messages = {'summary': {"required": "Пожалуйста, введите название"}}

    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 5:
            raise ValidationError("Это поле должно состоять из более 5 символов")
        return summary

    def clean(self):
        summary = self.cleaned_data.get('summary')
        description = self.cleaned_data.get('description')
        if summary and description and  summary == description:
            raise ValidationError("Описания не могут быть одинаковыми")
        return super(TaskForm, self).clean()
