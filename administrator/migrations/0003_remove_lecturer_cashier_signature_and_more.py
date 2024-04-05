# Generated by Django 5.0.2 on 2024-04-05 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_remove_lecturer_publication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='cashier_signature',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='date_received',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='phase',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='received_by',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='receiver_signature',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='semester',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='status',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='supervisor_approval_date',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='supervisor_comment',
        ),
        migrations.RemoveField(
            model_name='lecturer',
            name='voucher_number',
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lecturername',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='qualification',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]