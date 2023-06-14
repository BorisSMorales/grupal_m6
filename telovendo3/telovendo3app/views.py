from typing import Any, Dict
import uuid
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View

from telovendo3app.forms import FormularioContacto, LoginForm
from telovendo3app.models import Contacto

# Create your views here.

class HomeView(TemplateView):
    template_name = 'telovendo3app/home.html'

class ClientesView(View):
    template_name = 'telovendo3app/clientes.html'
    
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
    template_name = 'telovendo3app/contacto.html'

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

class Ingreso(TemplateView):
  template_name = 'registration/login.html'

  def get(self, request, *args, **kwargs):
    form = LoginForm()
    return render(request, self.template_name, { "form": form })
  
  def post(self, request, *args, **kwargs):
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username=username, password=password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('Home')
      form.add_error('username', 'Credenciales incorrectas')
      return render(request, self.template_name, { "form": form })
    else:
      return render(request, self.template_name, { "form": form })
    
    
class AreaRestringidaView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
  template_name = 'telovendo3app/restringido.html'
  permission_required = 'telovendo3app.puede_leer_formulario'
  def get(self, request, *args, **kwargs):
    titulo = "Restringido"
    contexto = {
      'titulo': titulo,
    }
    if titulo is None:
      return redirect('Home')
    return render(request, self.template_name, contexto)


class RegistroView(TemplateView):
    template_name = 'registration/registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect(self.success_url)

        return render(request, self.template_name, {'form': form})
