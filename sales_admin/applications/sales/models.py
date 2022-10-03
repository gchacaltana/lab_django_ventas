from django.db import models

# Create your models here.

class Currency(models.Model):
    """
    Clase Moneda.
    Ejemplo 1: Moneda Sol
    Código: PEN
    Simbolo: S/.
    Nombre: Sol Peruano

    Ejemplo 2: Moneda Dólares Americanos.
    Código: USD
    Simbolo: $.
    Nombre: Dólares Americanos
    """

    id = models.AutoField(primary_key=True)

    code = models.CharField(max_length=3,unique=True, verbose_name="Código")

    symbol = models.CharField(max_length=4, verbose_name="Simbolo")

    name = models.CharField(max_length=20, verbose_name="Nombre")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de Moficación")

    def __str__(self):
        return f"{self.symbol} {self.code}"

    class Meta:
        db_table = "currency"
        verbose_name = "Moneda"