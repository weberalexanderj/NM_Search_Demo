from django import forms


class CardDisplayForm(forms.Form):
    cards = forms.CharField(label='cards', max_length=100)
