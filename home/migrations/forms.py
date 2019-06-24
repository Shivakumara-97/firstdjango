from django import forms
class CustomForms(forms.From):
    username = forms.CharField(
        label = 'username',
        widget = forms.TextInput(
            attrs ={ 'placeholder':'you username',
            'class': 'form-control',

        )
    )
    email = form.EmailField(label="your Email",widget=forms.EmailIn)