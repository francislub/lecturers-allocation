# Generated by Django 5.0.2 on 2024-04-06 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0004_lecturer_courseunits_lecturer_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='semester',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
