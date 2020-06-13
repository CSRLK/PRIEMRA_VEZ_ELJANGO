from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .forms import Alumnoform, Gradoform, Seccionform, Inscripcionform
from .models import alumno, grado, seccion, inscripcion



#ALUMNO


class AlumnoList(ListView):
    model = alumno
    template_name = 'alumno/index.html'


class AlumnoCreate(CreateView):
    model = alumno
    template_name = 'alumno/create.html'
    form_class = Alumnoform
    success_url = reverse_lazy('alumno.index')


class AlumnoUpdate(UpdateView):
    model = alumno
    template_name = 'alumno/create.html'
    form_class = Alumnoform
    success_url = reverse_lazy('empleado.index')


class AlumnoDelete(DeleteView):
    model = alumno
    template_name = 'alumno/alumno_confirm_delete.html'
    success_url = reverse_lazy('alumno.index')



#GRADO
class GradoList(ListView):
    model = grado
    template_name = 'grado/index.html'


class GradoCreate(CreateView):
    model = grado
    template_name = 'grado/create.html'
    form_class = Gradoform
    success_url = reverse_lazy('grado.index')


class GradoUpdate(UpdateView):
    model = grado
    template_name = 'grado/create.html'
    form_class = Gradoform
    success_url = reverse_lazy('grado.index')


class GradoDelete(DeleteView):
    model = grado
    template_name = 'grado/grado_confirm_delete.html'
    success_url = reverse_lazy('grado.index')



#SECCION
class SeccionList(ListView):
    model = seccion
    template_name = 'seccion/index.html'


class SeccionCreate(CreateView):
    model = seccion
    template_name = 'seccion/create.html'
    form_class = Seccionform
    success_url = reverse_lazy('seccion.index')


class SeccionUpdate(UpdateView):
    model = seccion
    template_name = 'seccion/create.html'
    form_class = Seccionform
    success_url = reverse_lazy('seccion.index')


class SeccionDelete(DeleteView):
    model = seccion
    template_name = 'seccion/seccion_confirm_delete.html'
    success_url = reverse_lazy('seccion.index')


#INSCRIPCION
class InscripcionList(ListView):
    model = inscripcion
    template_name = 'inscripcion/index.html'


class InscripcionCreate(CreateView):
    model = inscripcion
    template_name = 'inscripcion/create.html'
    form_class = Inscripcionform
    success_url = reverse_lazy('inscripcion.index')


class InscripcionUpdate(UpdateView):
    model = inscripcion
    template_name = 'inscripcion/create.html'
    form_class = Inscripcionform
    success_url = reverse_lazy('inscripcion.index')


class InscripcionDelete(DeleteView):
    model = inscripcion
    template_name = 'inscripcion/inscripcion_confirm_delete.html'
    success_url = reverse_lazy('inscripcion.index')


