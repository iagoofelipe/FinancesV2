# Generated by Django 5.1.3 on 2024-11-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_infofield_optioninfofield_groupfield_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupfield',
            name='group_name',
            field=models.TextField(max_length=45, null=True),
        ),
    ]
