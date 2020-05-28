

from django.urls import path

from .views import views


urlpatterns = [
    path('', views.home, name="home"),
    path('pageUno/', views.pageUno, name='pageUno'),
    path('pageDos/', views.pageDos, name='pageDos'),
    path('pageTre/', views.pageTre, name='pageTre'),
    path('pageCuatro/', views.pageCuatro, name='pageCuatro'),
    path('pageCinco/', views.pageCinco, name='pageCinco')
]


