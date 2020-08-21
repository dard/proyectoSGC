from django.forms import *
from SGCapp.models import *


class ClienteForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = '__all__'
        # permite widgets personalizar
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Apellido',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nº de dni',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nº de telefono',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Email',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una direccón',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class CobradorForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cobrador
        fields = '__all__'
        # permite widgets personalizar
        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Nombre',
                }
            ),
            'apellido': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Apellido',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nº de dni',
                }
            ),
            'telefono': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nº de telefono',
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese un Email',
                }
            ),
            'direccion': TextInput(
                attrs={
                    'placeholder': 'Ingrese una direccón',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
