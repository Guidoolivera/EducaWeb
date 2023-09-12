from django import forms
from .models import Contacto, Inscripcion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'email', 'asunto', 'mensaje']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-horizontal mx-auto my-auto'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-6'
        self.helper.layout = Layout(
            Field('nombre_apellido', placeholder='Nombre y Apellido*'),
            Field('email', placeholder='Email*'),
            Field('asunto', placeholder='Asunto*'),
            Field('mensaje', placeholder='Mensaje*')
        )
        self.fields['nombre_apellido'].label = ''
        self.fields['email'].label = ''
        self.fields['asunto'].label = ''
        self.fields['mensaje'].label = ''


class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(InscripcionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'nombre',
            'apellido',
            'dni',
            'sexo',
            'email_tutor',
            'telefono_tutor',
            'curso_interes',
            Submit('submit', 'Enviar', css_class='btn btn-primary')
        )