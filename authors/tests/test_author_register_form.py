from unittest import TestCase
from authors.forms import RegisterForm
from parameterized import parameterized
from django.test import TestCase as DjangoTestCase


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your name'),
        ('email', 'Your e-mail'),
        ('first_name', 'Ex.: John'),
        ('last_name', 'Ex.: Doe'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_first_name_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        current_placeholder = form[field].field.widget.attrs['placeholder']
        print(placeholder)
        self.assertEqual(placeholder, current_placeholder)


class AuthorRegisterFormIntegrationTest(DjangoTestCase):
    def setup(self, *args, **kwargs):
        self.form_data = {
            'username': 'user',
            'first_name': 'first',
            'last_name': 'last',
            'email': 'email@anyemail.com',
            'password': 'StrongP@ssword1',
            'password2': 'StrongP@ssword1',
        }
        return super().setup(*args, **kwargs)
    
    @parameterized([
        ('username', 'Este campo e obrigatorio'),

    ])
    def test_fields_cannot_be_empty(self):
