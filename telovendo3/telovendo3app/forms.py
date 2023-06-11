from django import forms 

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=50, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'}),
                            error_messages={'required':'El nombre es obligatorio', 'max_length': 'el nombre no puede tener más de 50 caracteres'})
    email = forms.EmailField(label="Email", max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
                            error_messages={'required':'El Email es obligatorio', 'max_length':'el email no puede tener más de 100 caracteres'})
    empresa = forms.CharField(label='Empresa', max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Empresa', 'class':'form-control'}),
                            error_messages= {'required':'El nombre de la empresa es obligatorio', 'max_lenght':'El nombre de la empresa es muy largo'})
    asunto = forms.CharField(label='Asunto', max_length=100, required=True,
                            widget=forms.TextInput(attrs={'placeholder':'Asunto', 'class':'form-control'}),
                            error_messages= {'required':'El asunto es obligatorio', 'max_lenght':'El asunto no debe tener mas de 100 caracteres'})
    mensaje = forms.CharField(label ='Mensaje', max_length=1000, required = True,
                            widget=forms.Textarea(attrs={'placeholder':'mensaje', 'class':'form-control'}),
                            error_messages= {'required':'El mensaje es obligatorio', 'max_length':'El maximo de caracteres es de 1000'})

