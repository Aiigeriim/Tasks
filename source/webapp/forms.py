from django import forms
from django.forms import widgets
from webapp.models import status_choices


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
