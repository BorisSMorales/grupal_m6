from django import forms 

class FormularioContacto(forms.form):
    nombre = forms.CharField(label="nombre", max_length=50, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
                            error_messages={'required':}
    )


