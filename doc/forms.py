from django import forms
from .models import TextPdf

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class': 'input is-medium'}))
    first_name = None
    last_name = None
    username = forms.CharField(label="", max_length=20,
                               widget=forms.TextInput(attrs={'class': 'input is-medium'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'input is-medium'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = ('<span class="form-text text-muted"><small>Required. 150 characters or fewer. '
                                     'Letters, digits and @/./+/-/_ only.</small></span>')

        self.fields['password1'].widget.attrs['class'] = 'input is-medium'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = ('<ul class="form-text text-muted small"><li>Your password can\'t be too similar '
                                      'to your other personal information.</li><li>Your password must contain at least '
                                      '8 characters.</li><li>Your password can\'t be a commonly used '
                                      'password.</li><li>Your password can\'t be entirely numeric.</li></ul>')

        self.fields['password2'].widget.attrs['class'] = 'input is-medium'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = ('<span class="form-text text-muted"><small>Enter the same password as before, '
                                      'for verification.</small></span>')



class TextPdfForm(forms.ModelForm):
    class Meta:
        model = TextPdf
        fields = ['title', 'get', 'descr']
        labels = {
            'title': '',
            'get': '',
            'descr': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'input is-medium'}),
            'get': forms.URLInput(attrs={'class': 'input is-medium'}),
            'descr': forms.Textarea(attrs={'class': 'textarea is-medium', 'rows': '5'}),
        }
