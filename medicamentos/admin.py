from django.contrib import admin  # Herramientas para el panel administrativo.
from .models import Medicamento  # Importa el modelo que se mostrará en el panel.


# Registra Medicamento en el sitio de administración de Django.
@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidad", "precio")  # Columnas visibles en la lista administrativa.
    search_fields = ("nombre",)  # Habilita búsquedas por nombre.
