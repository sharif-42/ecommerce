# Generated by Django 4.1.6 on 2023-02-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='Product base image.', max_length=500, null=True, upload_to='product_images/%Y/%m/%d/', verbose_name='Image'),
        ),
    ]
