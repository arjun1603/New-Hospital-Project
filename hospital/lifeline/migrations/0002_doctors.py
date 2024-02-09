# Generated by Django 5.0.1 on 2024-01-30 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=100)),
                ('doc_spec', models.TextField()),
                ('doc_image', models.ImageField(default='..', upload_to='doctors')),
                ('dep_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lifeline.departments')),
            ],
        ),
    ]