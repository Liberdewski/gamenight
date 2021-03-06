from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class UserForm(forms.ModelForm):
    username = forms.CharField(
        label = 'Username',
        min_length = 6,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '6-30 Characters',
            }
        )
    )
    first_name = forms.CharField(
        label = 'First Name',
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    last_name = forms.CharField(
        label = 'Last Name',
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    email = forms.CharField(
        label = 'Email',
        required = True,
        widget=forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Email address',
            }
        )
    )
    password = forms.CharField(
        label = 'Password',
        min_length = 6,
        required = True,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '6+ Characters',
            }
        )
    )
    passwordretry = forms.CharField(
        label = 'Re-enter',
        min_length = 6,
        required = True,
        widget=forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '6+ Characters',
            }
        )
    )

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        passwordretry = cleaned_data.get("passwordretry")

        if password and passwordretry:
            if password !=passwordretry:
                msg = u"Passwords don't match"
                self._errors["password"] = self.error_class([msg])
                self._errors["passwordretry"] = self.error_class([msg])

                del cleaned_data["password"]
                del cleaned_data["passwordretry"]

        return cleaned_data

class EditUserForm(forms.ModelForm):
    username = forms.CharField(
        label = 'Username',
        min_length = 6,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '6-30 Characters',
            }
        )
    )
    first_name = forms.CharField(
        label = 'First Name',
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    last_name = forms.CharField(
        label = 'Last Name',
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    email = forms.CharField(
        label = 'Email',
        required = True,
        widget=forms.EmailInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Email address',
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Username',
        min_length = 6,
        required = True,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label = 'Password',
        min_length = 6,
        required = True,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
            }
        )
    )
    captcha = CaptchaField()
    
class ProfileForm(forms.ModelForm):
    addr_1 = forms.CharField(
        label='Address Line 1',
        min_length = 6,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    addr_2 = forms.CharField(
        label='Address Line 2',
        min_length = 6,
        required = False,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    city = forms.CharField(
        label='City',
        min_length = 6,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    prov = forms.CharField(
        label = 'Province',
        min_length = 2,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '2-5 Characters',
            }
        )
    )
    post_zip = forms.CharField(
        label = 'Postal Code',
        min_length = 2,
        required = True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'2-10 Characters',
            }
        )
    )
    class Meta:
        model = UserProfile
        fields = ('addr_1', 'addr_2', 'city', 'prov', 'post_zip',)


class EditProfileForm(forms.ModelForm):
    addr_1 = forms.CharField(
        label='Address Line 1',
        min_length = 6,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    addr_2 = forms.CharField(
        label='Address Line 2',
        min_length = 6,
        required = False,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    city = forms.CharField(
        label='City',
        min_length = 6,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '1-30 Characters',
            }
        )
    )
    prov = forms.CharField(
        label = 'Province',
        min_length = 2,
        required = True,
        widget=forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder': '2-5 Characters',
            }
        )
    )
    post_zip = forms.CharField(
        label = 'Postal Code',
        min_length = 2,
        required = True,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'2-10 Characters',
            }
        )
    )
    class Meta:
        model = UserProfile
        fields = ('addr_1', 'addr_2', 'city', 'prov', 'post_zip',)

    def save(self, commit=True):
        profile = super(ProfileForm, self).save(commit=False)
        profile.addr_1 = self.cleaned_data['addr_1']
        profile.addr_2 = self.cleaned_data['addr_2']
        profile.city = self.cleaned_data['city']
        profile.prov = self.cleaned_data['prov']
        profile.post_zip = self.cleaned_data['post_zip']

        if commit:
            profile.save()

        return profile