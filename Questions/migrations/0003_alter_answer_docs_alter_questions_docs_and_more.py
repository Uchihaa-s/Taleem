# Generated by Django 4.1.7 on 2023-03-03 22:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='docs',
            field=models.FileField(blank=True, null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='questions',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Images_uploaded'),
        ),
    ]
