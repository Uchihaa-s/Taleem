# Generated by Django 4.1.7 on 2023-03-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0003_alter_answer_docs_alter_questions_docs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Images_uploaded'),
        ),
    ]
