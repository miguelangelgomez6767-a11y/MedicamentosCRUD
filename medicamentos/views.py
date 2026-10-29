from django.urls import reverse_lazy  # Resuelve una URL por nombre de forma diferida.
from django.views.generic import CreateView, DeleteView, ListView, UpdateView  # Vistas genéricas para las operaciones CRUD.

from .models import Medicamento  # Importa el modelo que administra esta aplicación.


# Vista READ: consulta los medicamentos y los entrega a la plantilla de listado.
class MedicamentoListView(ListView):
    model = Medicamento  # Modelo del que se obtendrán los registros.
    template_name = "medicamentos/medicamento_list.html"  # Plantilla HTML que se renderiza.
    context_object_name = "medicamentos"  # Nombre de la colección disponible en la plantilla.


# Vista CREATE: muestra un formulario y crea un medicamento al enviarlo correctamente.
class MedicamentoCreateView(CreateView):
    model = Medicamento  # Modelo que se va a crear.
    fields = ["nombre", "cantidad", "precio"]  # Campos incluidos en el formulario.
    template_name = "medicamentos/medicamento_form.html"  # Plantilla compartida con la edición.
    success_url = reverse_lazy("medicamentos:lista")  # Destino después de guardar correctamente.


# Vista UPDATE: carga un medicamento existente y guarda los cambios enviados.
class MedicamentoUpdateView(UpdateView):
    model = Medicamento  # Modelo que se actualizará.
    fields = ["nombre", "cantidad", "precio"]  # Campos editables.
    template_name = "medicamentos/medicamento_form.html"  # Usa la misma plantilla de creación.
    success_url = reverse_lazy("medicamentos:lista")  # Regresa al listado tras actualizar.


# Vista DELETE: solicita confirmación y elimina el objeto tras una petición POST válida.
class MedicamentoDeleteView(DeleteView):
    model = Medicamento  # Modelo que se eliminará.
    template_name = "medicamentos/medicamento_confirm_delete.html"  # Pantalla de confirmación.
    success_url = reverse_lazy("medicamentos:lista")  # Regresa al listado tras eliminar.
