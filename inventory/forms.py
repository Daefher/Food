from django import forms
from .models import articulo

class articulo_model_form(forms.ModelForm):
    class Meta:
        model = articulo
        fields = [
            'nombre',
            'cantidad',
            'slug',
            'categoria',
            'fecha_creacion',
            'user'
        ]