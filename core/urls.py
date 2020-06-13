

from django.urls import path

from .class_view import AlumnoList, AlumnoUpdate, AlumnoDelete, GradoList, GradoCreate, GradoDelete, GradoUpdate, \
 AlumnoCreate, SeccionList, SeccionCreate, SeccionUpdate, SeccionDelete, InscripcionList, InscripcionCreate, \
 InscripcionUpdate, InscripcionDelete
from .views import views





urlpatterns = [
   path('', views.home, name="home"),
    #path('pageUno/', views.pageUno, name='pageUno'),
    #path('pageDos/', views.pageDos, name='pageDos'),
    #path('pageTre/', views.pageTre, name='pageTre'),
    #path('pageCuatro/', views.pageCuatro, name='pageCuatro'),
    #path('pageCinco/', views.pageCinco, name='pageCinco'),
    path('carrusel/index/', views.carrusel, name='carrusel.index'),

#EMPLEADO
    path('alumno/index/', AlumnoList.as_view(), name='alumno.index'),
    path('alumno/create/', AlumnoCreate.as_view(), name='alumno.create'),
    path('alumno/update/<int:pk>/', AlumnoUpdate.as_view(), name='alumno.update'),
    path('alumno/delete/<int:pk>/', AlumnoDelete.as_view(), name='alumno.delete'),


#GRADO
    path('grado/index/', GradoList.as_view(), name='grado.index'),
    path('grado/create/', GradoCreate.as_view(), name='grado.create'),
    path('grado/update/<int:pk>/', GradoUpdate.as_view(), name='grado.update'),
    path('grado/delete/<int:pk>/', GradoDelete.as_view(), name='grado.delete'),


#SECCION
    path('seccion/index/', SeccionList.as_view(), name='seccion.index'),
    path('seccion/create/', SeccionCreate.as_view(), name='seccion.create'),
    path('seccion/update/<int:pk>/', SeccionUpdate.as_view(), name='seccion.update'),
    path('seccion/delete/<int:pk>/', SeccionDelete.as_view(), name='seccion.delete'),


#INSCRIPCION
    path('inscripcion/index/', InscripcionList.as_view(), name='inscripcion.index'),
    path('inscripcion/create/', InscripcionCreate.as_view(), name='inscripcion.create'),
    path('inscripcion/update/<int:pk>/', InscripcionUpdate.as_view(), name='inscripcion.update'),
    path('inscripcion/delete/<int:pk>/', InscripcionDelete.as_view(), name='inscripcion.delete'),




]


