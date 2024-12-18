# Generated by Django 5.1.3 on 2024-11-19 18:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_registry_description_alter_registry_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=45),
        ),
        migrations.CreateModel(
            name='UserProfileRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.BooleanField(default=True)),
                ('edit', models.BooleanField(default=True)),
                ('read', models.BooleanField(default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='users',
            field=models.ManyToManyField(through='data.UserProfileRules', to=settings.AUTH_USER_MODEL),
        ),
    ]
