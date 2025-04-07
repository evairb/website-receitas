from django.urls import path
from authors import views

app_name = 'authors'
urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('register/create/', views.register_create, name="create"),
    path('intranet/', views.formulario_intra, name="intranet"),
    path('intranet/create/', views.formulario_intra_create, name="intranet_create"),

]
