from django import forms
from .models import alumno, grado, seccion, inscripcion




#ALUMNO
class Alumnoform(forms.ModelForm):
    class Meta:
        model=alumno
        fields="__all__"


#GRADO
class Gradoform(forms.ModelForm):
    class Meta:
        model=grado
        fields="__all__"


#SECCION
class Seccionform(forms.ModelForm):
    class Meta:
        model=seccion
        fields="__all__"


#INSCRIPCION
class Inscripcionform(forms.ModelForm):
    class Meta:
        model=inscripcion
        fields="__all__"


