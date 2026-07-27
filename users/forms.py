from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import CustomUser


class StyledAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'autofocus':True}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border rounded px-3 py-2 w-full outline-none'

class StyledUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border rounded px-3 py-2 w-full outline-none'
            self.fields['username'].help_text = "Required. Letters, digits and @/./+/-/_ only."
            self.fields['password1'].help_text = "At least 8 characters, not entirely numeric."
            self.fields['password2'].help_text = None
