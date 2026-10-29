from django.urls import path  # Función para declarar cada ruta.

# Importa las cuatro vistas que implementan el CRUD.
from .views import (
    MedicamentoCreateView,
    MedicamentoDeleteView,
    MedicamentoListView,
    MedicamentoUpdateView,
)

# Espacio de nombres para referenciar las rutas como medicamentos:lista, medicamentos:crear, etc.
app_name = "medicamentos"

# Mapa de URL a vista.
urlpatterns = [
    path("", MedicamentoListView.as_view(), name="lista"),  # GET /: lista los medicamentos.
    path("nuevo/", MedicamentoCreateView.as_view(), name="crear"),  # /nuevo/: formulario de creación.
    path("<int:pk>/editar/", MedicamentoUpdateView.as_view(), name="editar"),  # pk identifica el medicamento a editar.
    path("<int:pk>/eliminar/", MedicamentoDeleteView.as_view(), name="eliminar"),  # pk identifica el medicamento a eliminar.
]
