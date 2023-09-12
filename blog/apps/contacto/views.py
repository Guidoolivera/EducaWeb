from typing import Any, Dict
from django.shortcuts import render, redirect
from .forms import ContactoForm, InscripcionForm
from django.contrib import messages
from django.views.generic import CreateView 
from django.urls import reverse_lazy
from crispy_forms.utils import render_crispy_form

# Create your views here.

class ContactoUsuario(CreateView):
    template_name= 'contacto/contacto.html'
    form_class= ContactoForm
    success_url= reverse_lazy('apps.posts:posts')#

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        messages.success(self.request, 'Consulta enviada.')
        return super().form_valid(form)
    
def inscripcion_view(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos del formulario, como guardarlos en la base de datos
            # Por ahora, simplemente redirigimos a una página de confirmación
            return redirect('confirmacion_inscripcion')
    else:
        form = InscripcionForm()
    
    # Renderiza el formulario con crispy
    form_html = render_crispy_form(form)

    context = {'form': form}
    return render(request, 'inscribirse/inscribirse.html', context)