#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template


class views():

    def home(self):

        plantilla = get_template('core/base.html')
        return HttpResponse(plantilla.render())

    def pageUno(self):
        plantilla = get_template('core/pageUno.html')
        return HttpResponse(plantilla.render())

    def pageDos(self):
        plantilla = get_template('core/pageDos.html')
        return HttpResponse(plantilla.render())

    def pageTre(self):
        plantilla = get_template('core/pageTre.html')
        return HttpResponse(plantilla.render())

    def pageCuatro(self):
        plantilla = get_template('core/pageCuatro.html')
        return HttpResponse(plantilla.render())

    def pageCinco(self):
        plantilla = get_template('core/pageCinco.html')
        return HttpResponse(plantilla.render())


