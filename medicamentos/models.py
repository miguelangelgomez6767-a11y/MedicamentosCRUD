from django.db import models  # Importa los tipos de campos y la clase base de los modelos Django.
from django.core.validators import MinValueValidator  # Validador que establece un valor mínimo.


# Modelo que representa un medicamento guardado en la base de datos.
class Medicamento(models.Model):
    # Nombre del medicamento; admite texto de hasta 150 caracteres.
    nombre = models.CharField("nombre", max_length=150)
    # Cantidad disponible; es un campo entero no negativo.
    cantidad = models.PositiveIntegerField("cantidad")
    # Precio con hasta 10 dígitos en total y 2 decimales.
    precio = models.DecimalField(
        "precio",
        max_digits=10,#total de dígitos
        decimal_places=2, #  está configurado para centavos
        validators=[MinValueValidator(0)],  # Durante la validación, impide precios menores que cero.
    )

    # Opciones adicionales del modelo.
    class Meta:
        ordering = ["nombre"]  # Orden predeterminado alfabético por nombre.
        verbose_name = "medicamento"  # Nombre singular legible.
        verbose_name_plural = "medicamentos"  # Nombre plural legible.

    # Define la representación textual del objeto, útil en el administrador y en depuración.
    def __str__(self):
        return self.nombre  # Muestra el nombre en vez de una representación genérica.
