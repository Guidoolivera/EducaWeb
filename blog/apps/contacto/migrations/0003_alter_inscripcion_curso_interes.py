# Generated by Django 4.2.4 on 2023-09-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_inscripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='curso_interes',
            field=models.CharField(choices=[('Jardin', 'Educación Inicial'), ('Educacion', 'Educación Primaria'), ('Secundaria', 'Educación Secundaria')], max_length=20),
        ),
    ]
