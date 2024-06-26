import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('coursename', models.CharField(blank=True, max_length=300, null=True)),
                ('semester', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('lecturername', models.CharField(blank=True, max_length=200, null=True, validators=[django.core.validators.RegexValidator('^[A-Za-z\\s]+$', 'Only letters and spaces allowed for lecturer name')])),
                ('qualification', models.CharField(blank=True, choices=[('D', 'Degree'), ('DM', 'Degree - Masters'), ('DMP', 'Degree - Masters - PhD')], max_length=255, null=True)),
                ('publication', models.CharField(blank=True, choices=[('N', 'None '), ('1', '1 to 2 Papers'), ('3', '3 to 4 Papers'), ('5', '5 to 6 Papers'), ('7', '7 to 8 Papers'), ('9', '9 and above')], max_length=255, null=True)),
                ('semester', models.CharField(blank=True, choices=[('F', 'First Semester'), ('S', 'Second Semester')], max_length=10, null=True)),
                ('received_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_received', models.DateTimeField(blank=True, null=True)),
                ('cashier_signature', models.ImageField(blank=True, null=True, upload_to='cashier_signatures/')),
                ('receiver_signature', models.ImageField(blank=True, null=True, upload_to='receiver_signatures/')),
                ('voucher_number', models.CharField(blank=True, max_length=100, null=True)),
                ('supervisor_comment', models.TextField(blank=True)),
                ('supervisor_approval_date', models.DateTimeField(blank=True, null=True)),
                ('phase', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('Pending Supervisor Approval', 'Pending Supervisor Approval'), ('Pending Approver Approval', 'Pending Approver Approval'), ('Business Approval 1', 'Business Approval 1'), ('Business Approval 2', 'Business Approval 2'), ('Business Approval 3', 'Business Approval 3'), ('Approved', 'Approved'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('Cash Out', 'Cash Out')], default='Pending Supervisor Approval', max_length=30)),
            ],
        ),
    ]
