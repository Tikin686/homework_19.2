from django.db import models
from users.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименования'
    )
    description = models.TextField(
        verbose_name='Описание'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Наименование'
    )
    description = models.CharField(
        max_length=100,
        verbose_name='Описание'
    )
    photo = models.ImageField(
        upload_to='catalog/image',
        blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Категория'
    )
    price = models.FloatField(
        verbose_name='Цена покупки'
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания', auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего изменения', auto_now=True
    )
    owner = models.ForeignKey(User, verbose_name="products", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="versions",
        verbose_name="product",
    )
    version_number = models.CharField(max_length=50, verbose_name="Номер версии")
    version_name = models.CharField(max_length=150, verbose_name="Название версии")
    is_current = models.BooleanField(default=False, verbose_name="Признак текущей версии")


class Meta:
    version_name = "Версия"
    version_name_plural = "Версии"
    ordering = ["product", ]

    def __str__(self):
        return f"{self.product.name} - {self.version_name} ({self.version_number})"
