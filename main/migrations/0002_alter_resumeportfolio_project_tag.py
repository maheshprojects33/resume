# Generated by Django 4.1.7 on 2023-03-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeportfolio',
            name='project_tag',
            field=models.CharField(blank=True, default=None, max_length=10),
        ),
    ]
