from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя', 'class': 'form-control valid'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail', 'class': "form-control w-100"}
        )
    )

    messege = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение', 'cols': 30, 'rows': 9, 'class': "form-control w-100"}
        )
    )