# Generated by Django 3.0.3 on 2020-06-04 04:05

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100)]), size=6)),
                ('final_score', models.FloatField(null=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='students.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subjects.Subject')),
            ],
        ),
    ]
