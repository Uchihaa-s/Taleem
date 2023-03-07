# Generated by Django 4.1.7 on 2023-03-03 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Questions', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('Tittle', models.CharField(max_length=266)),
                ('catogery', models.ManyToManyField(to='Questions.catogery')),
            ],
        ),
    ]