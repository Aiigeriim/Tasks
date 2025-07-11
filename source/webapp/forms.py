# from django import forms
# from django.core.exceptions import ValidationError
# from django.forms import widgets
# from django.utils import timezone

# from webapp.models import Task


# class TaskForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     for field in self.fields.values():
    #         field.widget.attrs['class'] = 'form-control'

    # class Meta:
    #     model = Task
    #     # exclude = ('completion_date', 'published_at')
    #     fields = ('name', 'description', 'status', 'completion_date', 'published_at', 'tags')
    #     widgets = {
    #         # 'published_at':  widgets.DateTimeInput(
    #         #     attrs={'type': 'datetime-local'}),
    #         'completion_date': widgets.DateInput(
    #             attrs={'type': 'date'}),
    #         # 'tags': forms.ModelChoiceField(),
            # 'comments': forms.Textarea(),
        # }
        # error_messages = {'title': {"required": "Пожалуйста, введите название"}}

    # def clean_published_at(self):
    #     published_at = self.cleaned_data['published_at']
    #     if not published_at:
    #         raise ValidationError("заполните это поле")
    #     if published_at < timezone.now():
    #         raise ValidationError("This date is in the future")
    #     return published_at

    # def clean(self):
    #     name = self.cleaned_data.get('name')
    #     description = self.cleaned_data.get('description')
    #     if name and description and  name == description:
    #         raise ValidationError("Название и описание не могут быть одинаковыми")
    #     return super(TaskForm, self).clean()