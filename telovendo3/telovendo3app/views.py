from typing import Any, Dict
import uuid
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views import View

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
