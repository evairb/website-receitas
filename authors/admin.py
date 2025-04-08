from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.CategoriaProfissional)
class CategoriaProfissional(admin.ModelAdmin):
    ...


@admin.register(models.LocalTrabalho)
class LocalTrabalho(admin.ModelAdmin):
    ...


@admin.register(models.CoordenadoriaHospitalMunicipal)
class CoordenadoriaHospitalMunicipal(admin.ModelAdmin):
    ...


@admin.register(models.SupervisaoTecnica)
class SupervisaoTecnica(admin.ModelAdmin):
    ...
