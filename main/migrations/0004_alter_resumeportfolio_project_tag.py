# Generated by Django 4.1.7 on 2023-03-16 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_resumeportfolio_project_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumeportfolio',
            name='project_tag',
            field=models.CharField(blank=True, choices=[('code', 'code'), ('graphics', 'graphics'), ('3d', '3d')], default='', max_length=10),
        ),
    ]
