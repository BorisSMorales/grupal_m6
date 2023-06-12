from typing import Any, Dict
import uuid
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views import View

from telovendo3.telovendo3app.forms import FormularioContacto
from telovendo3.telovendo3app.models import Contacto

# Create your views here.

class HomeView(TemplateView):
    template_name = 'telovendo3app/base.html'

class ClientesView(View):
    template_name = 'clientes.html'
    
    def get(self, request, *args, **kwargs):
        # Lógica para obtener los datos de los clientes
        clientes_data = [
            {'nombre': 'Sofía', 'apellido': 'González', 'correo': 'sofia@example.com', 'telefono': '+56 9 12345678', 'ciudad': 'Santiago', 'ultima_compra': '2023-05-15'},
            {'nombre': 'Sebastián', 'apellido': 'López', 'correo': 'sebastian@example.com', 'telefono': '+56 9 98765432', 'ciudad': 'Valparaíso', 'ultima_compra': '2023-06-01'},
            {'nombre': 'Valentina', 'apellido': 'Silva', 'correo': 'valentina@example.com', 'telefono': '+56 9 56789012', 'ciudad': 'Concepción', 'ultima_compra': '2023-05-28'},
            {'nombre': 'Matías', 'apellido': 'Pereira', 'correo': 'matias@example.com', 'telefono': '+56 9 43210987', 'ciudad': 'Antofagasta', 'ultima_compra': '2023-05-20'},
            {'nombre': 'Isabella', 'apellido': 'Martínez', 'correo': 'isabella@example.com', 'telefono': '+56 9 90123456', 'ciudad': 'La Serena', 'ultima_compra': '2023-05-31'},
        ]
        return render(request, self.template_name, {'clientes': clientes_data})


class ContactoView(TemplateView):
    template_name = 'contacto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = FormularioContacto()
        return context

    def post(self, request, *args, **kwargs):
        form = FormularioContacto(request.POST)
        mensajes = {
            "enviado": False,
            "resultado": None
        }
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            empresa = form.cleaned_data['empresa']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            registro = Contacto(
                nombre=nombre,
                email=email,
                empresa=empresa,
                asunto=asunto,
                mensaje=mensaje
            )
            registro.save()

            mensajes = { "enviado": True, "resultado": "Mensaje enviado correctamente" }
        else:
            mensajes = { "enviado": False, "resultado": form.errors }
        return render(request, self.template_name, { "formulario": form, "mensajes": mensajes })





