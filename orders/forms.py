from django import forms

from orders.models import Order

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'placeholder': 'you@example.com'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'placeholder': 'Жетису, дом 50'}))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address')