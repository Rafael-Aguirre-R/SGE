# Generated by Django 3.0.3 on 2020-06-03 19:40

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.TextField()),
                ('gen_comp_develop', models.TextField()),
                ('scheduled_sessions', models.IntegerField()),
                ('real_sessions', models.IntegerField()),
                ('unit_assess_session', models.IntegerField()),
                ('real_assess_session', models.IntegerField()),
                ('learning_activity', models.TextField()),
                ('teaching_activity', models.TextField()),
                ('generic_competences', models.TextField()),
                ('reprobation', models.IntegerField()),
                ('desertion', models.IntegerField()),
                ('review_date', models.DateTimeField()),
                ('observations', models.TextField()),
                ('subtopics', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('practices', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('didactic_support', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('required_equipment', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('information_sources', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='subjects.Subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequiredVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('destination', models.CharField(max_length=100)),
                ('workplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work_plans.Workplan')),
            ],
        ),
    ]