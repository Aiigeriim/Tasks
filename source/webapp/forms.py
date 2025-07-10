from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils import timezone

from webapp.models import status_choices

# def published_at_validate(value):
#     if value < timezone.now():
#         raise forms.ValidationError('This date is in the future')




class TaskForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label="Название",
        widget=widgets.Input(
        attrs={'class': 'form-control'}),
        error_messages={"required": "Пожалуйста, введите название"},

    )
    description = (forms.CharField(
        widget=forms.Textarea(
        attrs={"cols": "25", "rows": "5", "class": "form-control"}),
        required=False,
        label="Описание"))
    status = forms.ChoiceField(
        choices=status_choices,
        label='Статус',
        initial='new',
        widget=forms.Select(
        choices=status_choices,
        attrs={'class': 'form-control'}))
    completion_date = forms.DateField(
        required=False,
        label='Дэдлайн',
        widget=forms.DateInput(
            attrs={'type': 'date','class': 'form-control'}))

    published_at = forms.DateTimeField(
        required=False,
        label='Дата публикации',
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local', 'class': 'form-control'}),
        # validators=[published_at_validate],
    )

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