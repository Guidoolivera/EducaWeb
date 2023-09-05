# Generated by Django 4.2.4 on 2023-09-04 00:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('subtitulo', models.CharField(blank=True, max_length=80, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='usuario')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(default='Sin categoía', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.categoria')),
            ],
            options={
                'ordering': ('publicado',),
            },
        ),
    ]
