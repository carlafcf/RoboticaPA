# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth import forms as auth_forms
from django import forms
from django.forms import ModelForm

from Usuario.models import Usuario


class FormCriarUsuario(auth_forms.UserCreationForm):

    class Meta:
        # fields = ('cidade', 'estado')
        fields = ('username', 'first_name', 'last_name', 'email', 'cidade', 'estado', 'password1', 'password2')
        model = Usuario

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].label = 'Nome'
    #     self.fields['last_name'].label = 'Sobrenome'
    #     self.fields['username'].label = 'Nome de usuário'
    #     self.fields['email'].label = 'E-mail'
    #     self.fields['password1'].label = 'Senha'
    #     self.fields['password2'].label = 'Confirmar senha'

# class EditarUsuarioForm(ModelForm):
#     password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 'email')

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("As senhas estão incorretas.")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super(EditarUsuarioForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         # user.active = False # send confirmation email
#         if commit:
#             user.save()
#         return user