from django import forms
from django.contrib.auth import forms as auth_forms
from apps.league import models
from crispy_forms.helper import FormHelper

class AuthenticationForm(auth_forms.AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type your username',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Type your password'
            }
        )
    )

    # Defining custom error message for invalid login.
    error_messages = {
        'invalid_login': ("Invalid username and/or password."),
    }

    # Verify that the user is active before allowing login.
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("This account is still inactive.", code='inactive', )

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class UserCreationForm(auth_forms.UserCreationForm):
    # A form for creating new users. It includes an additional field not used by default (email).
    class Meta:
        model = models.LeagueUser
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)


class UserChangeForm(auth_forms.UserChangeForm):
    # A form for updating new users.
    class Meta:
        model = models.LeagueUser
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
