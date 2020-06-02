from django.contrib.auth.models import User
from django import forms


class RegisterFrom(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        # forms.ModelForm에게 상속받은 클래스에서 User테이블의 데이터 필드를 쉽게 지정할 수 있다..?
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password2']
