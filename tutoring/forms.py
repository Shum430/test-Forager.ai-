from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.exceptions import ValidationError

from tutoring.models import Pupil
from utils.email_utils import validate_email_with_hunter


class PupilLoginForm(AuthenticationForm):
    pass


class PupilRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Pupil
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email",)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        # Check email validity using Hunter API
        if not validate_email_with_hunter(email):
            self.add_error('email', 'Invalid email address. Please provide a valid email.')
            raise ValidationError("")

        return email
