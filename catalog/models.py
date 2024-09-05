from django.db import models

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
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

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
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата последнего изменения'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', ['name']]

    def __str__(self):
        return self.name