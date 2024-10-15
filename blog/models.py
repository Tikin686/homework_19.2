from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Загаловок")
    slug = models.CharField(max_length=150, verbose_name="slug", blank=True, null=True)
    text = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="catalog/media", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["title", ]

    def __str__(self):
        return self.title
