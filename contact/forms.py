from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                # 'placeholder': 'Here came from init',
            }
        ),
        label='First name',
        help_text='help-text for the user',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Here came from init',
        # })

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category',
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Write here',
        #         }
        #     )
        # }

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                "The last name can't be the same as the first name",
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if any(char.isdigit() for char in first_name):
            self.add_error(
                'first_name',
                ValidationError(
                    "Don't insert numbers in a name",
                    code='invalid'
                )
            )

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    "A name can't be 'ABC'",
                    code='invalid'
                )
            )

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if any(char.isdigit() for char in last_name):
            self.add_error(
                'last_name',
                ValidationError(
                    "Don't insert numbers in a name",
                    code='invalid'
                )
            )

        if last_name == 'ABC':
            self.add_error(
                'last_name',
                ValidationError(
                    "A name can't be 'ABC'",
                    code='invalid'
                )
            )

        return last_name
