from django import forms
from django.contrib.auth.models import User

class RegistrarUsuarioForm(forms.Form):

    nome = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    senha = forms.CharField(required=True)
    telefone = forms.CharField(required=True)
    nome_empresa = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(RegistrarUsuarioForm, self).is_valid():
            self.adicionar_erro('Por favor, verifique os dados informados.')
            valid = False

        user_exists = User.objects.filter(username=self.data['nome']).exists()
        if user_exists:
            self.adicionar_erro('Usuario ja existe em nossa base de dados.')
            valid = False

        return valid

    def adicionar_erro(self, message):
        error = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        error.append(message)