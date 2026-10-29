from django.test import TestCase  # Clase base que crea una base de datos aislada para las pruebas.
from django.urls import reverse  # Obtiene las URL a partir de sus nombres.

from .models import Medicamento  # Modelo que se pondrá a prueba.


# Conjunto de pruebas automáticas para las operaciones principales del CRUD.
class MedicamentoCrudTests(TestCase):
    # Prepara un medicamento de ejemplo antes de ejecutar cada prueba.
    def setUp(self):
        self.medicamento = Medicamento.objects.create(
            nombre="Paracetamol",
            cantidad=20,
            precio="35.50",
        )

    # Comprueba que la lista cargue y muestre los datos del medicamento.
    def test_lista_consulta_medicamentos(self):
        response = self.client.get(reverse("medicamentos:lista"))  # Simula una solicitud GET al listado.

        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea exitosa.
        self.assertContains(response, "Paracetamol")  # Verifica que aparezca el nombre.
        self.assertContains(response, "35.50")  # Verifica que aparezca el precio formateado.

    # Comprueba que se pueda crear un medicamento enviando un formulario POST.
    def test_crea_medicamento(self):
        response = self.client.post(
            reverse("medicamentos:crear"),  # URL de la vista de creación.
            {"nombre": "Ibuprofeno", "cantidad": 10, "precio": "42.00"},  # Datos del formulario.
        )

        self.assertRedirects(response, reverse("medicamentos:lista"))  # Verifica la redirección tras guardar.
        self.assertTrue(Medicamento.objects.filter(nombre="Ibuprofeno").exists())  # Confirma que el registro exista.

    # Comprueba que se actualicen los campos de un medicamento existente.
    def test_modifica_medicamento(self):
        response = self.client.post(
            reverse("medicamentos:editar", args=[self.medicamento.pk]),  # URL de edición con la clave primaria.
            {"nombre": "Paracetamol 500 mg", "cantidad": 30, "precio": "40.00"},  # Nuevos valores.
        )

        self.assertRedirects(response, reverse("medicamentos:lista"))  # Verifica la redirección.
        self.medicamento.refresh_from_db()  # Recarga el objeto con los datos guardados en la base de datos.
        self.assertEqual(self.medicamento.nombre, "Paracetamol 500 mg")  # Comprueba el nombre actualizado.
        self.assertEqual(self.medicamento.cantidad, 30)  # Comprueba la cantidad actualizada.

    # Comprueba que el registro desaparezca después de confirmar la eliminación.
    def test_elimina_medicamento(self):
        response = self.client.post(
            reverse("medicamentos:eliminar", args=[self.medicamento.pk])  # Envía POST a la ruta del objeto.
        )

        self.assertRedirects(response, reverse("medicamentos:lista"))  # Verifica la redirección tras borrar.
        self.assertFalse(Medicamento.objects.filter(pk=self.medicamento.pk).exists())  # Comprueba que ya no exista.
