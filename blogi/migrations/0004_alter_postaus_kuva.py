# Generated by Django 4.1.6 on 2023-03-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0003_postaus_kuva'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postaus',
            name='kuva',
            field=models.ImageField(null=True, upload_to='blogi/kuvat'),
        ),
    ]
