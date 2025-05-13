from django import forms
from django. contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from authors.validators import AuthorRecipeValidator


def add_attr(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def strong_password(password):
    regex = re.compile(r'(?=.*[a-z])(?=.*[a-z])(?=.*[0-9]).{8,}$')

    if not regex.match(password):
        raise ValidationError((
            'Password must have at least one uppervase letter,'
            'on lowercase letter and one number. The length should be'
            'at least 8 characters.'
            ),
            code='Invalid'
        )


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your name')
        add_placeholder(self.fields['email'], 'Your e-mail')
        add_placeholder(self.fields['first_name'], 'Ex.: John')
        add_placeholder(self.fields['last_name'], 'Ex.: Doe')
        add_placeholder(self.fields['password'], 'Type your password')
        add_placeholder(self.fields['password2'], 'Repeat your password')

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(),
        validators=[strong_password]
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        # exclude = ['first_name']
        labels = {
            'username': 'Username',
            'email': 'E-mail',
            'first_name': 'First name',
        }
        help_text = {
            'email': 'The e-mail must be valid'
        }
        error_message = {
            'username': {
                'required': 'This field must not be empty',
                'max_lenght': 'This field must have less than 3 caracteres',
            }
        }
        # controla o widget
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input text-input outra-classe'
            }),
        }

    def clean_password(self):
        data = self.cleaned_data.get('password')

        if 'atencao' in data:
            raise ValidationError(
                'Nao digite %(value)s no campo de password',
                code='invalid',
                params={'value': '"atencao"'}
            )
        return data

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User email is already in use', code='invalid'
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'As senhas precisao ser iguais'
            })
        return cleaned_data


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your username')
        add_placeholder(self.fields['password'], 'Type your password')
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )


class AuthorRecipeForm(forms.ModelForm):
    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        AuthorRecipeValidator(self.cleaned_data, ErrorClass=ValidationError)

        return super_clean
