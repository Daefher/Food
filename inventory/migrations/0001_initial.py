# Generated by Django 2.2 on 2019-04-15 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, null=True)),
                ('cantidad', models.IntegerField(null=True)),
                ('slug', models.SlugField(max_length=128, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('fecha_creacion', models.DateField(null=True)),
                ('categoria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.categoria')),
                ('user', models.ForeignKey(blank=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
