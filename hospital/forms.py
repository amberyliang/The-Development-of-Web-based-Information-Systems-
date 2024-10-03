from django import forms
from .models import Registration
from . import models
from captcha.fields import CaptchaField
class RegistrationForm(forms.Form):
    GENDER_CHOICES = [
        ('Male', '男'),
        ('Female', '女'),
    ]

    name = forms.CharField(label='姓名')
    birthday = forms.DateField(label='生日', widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(label='性別', choices=GENDER_CHOICES)
    id_number = forms.CharField(label='身分證字號', max_length=10)
    phone_number = forms.CharField(label='連絡電話', max_length=10)


    def clean_id_number(self):
        id_number = self.cleaned_data['id_number']
        if len(id_number) != 10:
            raise forms.ValidationError('身分證字號必須為十個字')
        return id_number

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if len(phone_number) != 10:
            raise forms.ValidationError('連絡電話必須為十個字')
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        id_number = cleaned_data.get('id_number')
        if id_number:
            existing_registration = Registration.objects.filter(id_number=id_number).exists()
            if existing_registration:
                raise forms.ValidationError('該身分證字號已經登記過')
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='姓名', max_length=10)
    password = forms.CharField(label='密碼', widget = forms.PasswordInput())


class UserRegistrationForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.User
        fields = ['name','email','password']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm,self).__init__(*args,**kwargs)
        self.fields['name'].label = '使用者姓名'
        self.fields['email'].label = 'Email'
        self.fields['password'].label = '使用者密碼'
        self.fields['captcha'].label = '驗證'

