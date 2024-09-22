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

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Загаловок")
    slug = models.CharField(max_length=150, verbose_name="slug")
    text = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="catalog/media", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    views_count = models.ImageField(default=0, verbose_name="Просмотры")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")


    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", ]

    def __str__(self):
        return self.title