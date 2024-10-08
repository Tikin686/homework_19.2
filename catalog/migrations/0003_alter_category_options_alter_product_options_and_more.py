# Generated by Django 5.1 on 2024-09-08 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_rename_create_data_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'name'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='manufactured_at',
        ),
    ]
