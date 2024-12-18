# Generated by Django 5.1.3 on 2024-11-19 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='registry',
            name='title',
            field=models.TextField(blank=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='registry',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=11),
        ),
    ]
