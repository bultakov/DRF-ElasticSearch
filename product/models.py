from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255, verbose_name="Mahsulot turi")
    volume = models.FloatField(verbose_name="Mahsulot hajmi")
    description = models.TextField(verbose_name="Mahsulot haqida ma'lumot")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
