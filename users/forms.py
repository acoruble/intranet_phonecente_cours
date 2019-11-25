from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import UserProfile

class FormWithSubmit(forms.Form):
    helper = FormHelper()
    helper.add_input(Submit('submit', "Valider", css_class="btn btn-lg btn-primary btn-block bg_main"))
    helper.form_method = 'POST'

class ModelFormWithSubmit(forms.ModelForm):
    helper = FormHelper()
    helper.add_input(Submit('submit', "Valider", css_class="btn btn-lg btn-primary btn-block bg_main"))
    helper.form_method = 'POST'

class RegisterForm(FormWithSubmit):
    username = forms.CharField(
        label = "Nom d'utilisateur",
        max_length=64,
        required=True,
        )
    email = forms.EmailField(
        label = "Adresse Email",
        max_length=256,
        required=True,
        )
    raw_password = forms.CharField(
        label = "Mot de passe",
        max_length=256,
        required=True,
        help_text = "10 caractères minimums",
        widget=forms.PasswordInput(),
    )
    raw_password_confirmation = forms.CharField(
        label = "Mot de passe (confirmation)",
        max_length=256,
        required=True,
        widget=forms.PasswordInput(),
        )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        raw_password = cleaned_data.get('raw_password')
        raw_password_confirmation = cleaned_data.get('raw_password_confirmation')
        if len(raw_password) < 10:
            raise forms.ValidationError("Le mot de passe doit faire 10 caractères minimum")
        if raw_password and raw_password_confirmation:
            if raw_password != raw_password_confirmation:
                raise forms.ValidationError("Les mots de passe ne sont pas identiques")
        try:
            UserProfile.objects.get(username=cleaned_data['username'])
        except UserProfile.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Cet utilisateur existe déjà")

        try:
            UserProfile.objects.get(email=cleaned_data['email'])
        except UserProfile.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Cet utilisateur existe déjà")

        return cleaned_data

class AccountSettingsForm(ModelFormWithSubmit):

    # Facultatif
    display_name = forms.CharField(
        label = "Nom d'affichage",
        max_length=256,
        )

    class Meta:
        model = UserProfile
        fields = ('display_name', 'newsletter_agreement', )
