from django.db import models

# Create your models here.

#ALUMNOS

class alumno(models.Model):
    nombre=models.CharField(max_length=30, default='')
    apellido=models.CharField(max_length=30, default='')
    edad=models.CharField(max_length=20, default='')

    def __str__(self):
        return '%s' % self.nombre

#GRADO
class grado(models.Model):
    nombre=models.CharField(max_length=30, default='')
    nivel=models.CharField(max_length=30, default='')

    def __str__(self):
        return '%s' % self.nombre

#SECCION
class seccion(models.Model):
    nombre=models.CharField(max_length=30, default='')

    def __str__(self):
        return '%s' % self.nombre


#INSCRIPCION

class inscripcion(models.Model):

    alumno = models.ForeignKey(alumno, on_delete=models.CASCADE, default='')
    grado = models.ForeignKey(grado, on_delete=models.CASCADE, default='')
    seccion = models.ForeignKey(seccion, on_delete=models.CASCADE, default='')

    def __str__(self):
        return '%s' % self.alumno.nombre




