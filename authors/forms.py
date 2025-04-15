from django import forms
from django. contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from . import models
from utils.valida_cpf import valida_cpf


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


class InformacoesPessoalForm(forms.ModelForm):
    class Meta:
        model = models.InformacoePessoal
        fields = '__all__'
        validation_error_msgs = {}
        widgets = {
            'cpf': forms.TextInput(attrs={
                'placeholder': '12345678900',
                # 'data-mask': '000.000.000-00',
            }),
            'fone': forms.TextInput(attrs={
                'placeholder': '(00)00000-0000',
                # 'data-mask': '(00)00000-0000',
            }),
        }

    def clean(self, *args, **kwargs):
        cleaned = super().clean()

        cpf_data = cleaned.get('cpf')
        nome_data = cleaned.get('nome')
        sobrenome_data = cleaned.get('sobrenome')
        cidade_data = cleaned.get('cidade')
        pais_data = cleaned.get('pais')
        fone_data = cleaned.get('fone')
        rg_data = cleaned.get('rg')
        nome_social_data = cleaned.get('nome_social')
        ramal_data = cleaned.get('ramal')

        if cpf_data:
            if not valida_cpf(cpf_data):
                self.add_error('cpf', 'CPF invalido.')

            if len(cpf_data) < 11:
                self.add_error('cpf', 'CPF deve conter 11 dígitos.')

        if nome_data:
            if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome_data):
                self.add_error(
                    'nome', 'Nome deve conter apenas letras e espaços.'
                )
            if len(nome_data) > 50:
                self.add_error('nome', 'nome muito longo.')

        if sobrenome_data:
            if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', sobrenome_data):
                self.add_error(
                    'sobrenome', 'Nome deve conter apenas letras e espaços.'
                )
            if len(sobrenome_data) > 80:
                self.add_error('sobrenome', 'sobrenome muito longo.')

        if cidade_data:
            if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', cidade_data):
                self.add_error(
                    'cidade', 'cidade deve conter apenas letras e espaços.'
                )

        if pais_data:
            if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', pais_data):
                self.add_error(
                    'pais', 'Pais deve conter apenas letras e espaços.'
                )

        if fone_data:
            fone_limpo = re.sub(r'\D', '', fone_data)
            if len(fone_limpo) < 10 or len(fone_limpo) > 11:
                self.add_error(
                    'fone', 'Numero deve conter 10 digitos para Fixo.'
                )
                self.add_error(
                    'fone', 'Numero deve conter 11 digitos para Celular.'
                )
            if not fone_limpo.isdigit():
                self.add_error('fone', 'Número de fone inválido.')

        if rg_data:
            if len(rg_data) < 7 or len(rg_data) > 12:
                self.add_error('rg', 'rg invalido.')

        if nome_social_data:
            if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', sobrenome_data):
                self.add_error(
                    'nome_social',
                    'Nome Social deve conter apenas letras e espaços.'
                )

        if ramal_data:
            if not re.match(r'^\d+$', ramal_data):
                self.add_error('ramal', 'Ramal deve conter apenas digitos.')

        return cleaned


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Type your username')
        add_placeholder(self.fields['password'], 'Type your password')
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
