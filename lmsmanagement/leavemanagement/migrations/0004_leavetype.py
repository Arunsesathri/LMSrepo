# Generated by Django 4.2.8 on 2024-01-16 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leavemanagement', '0003_userdetails_designation_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavetype', models.CharField(max_length=255)),
                ('leavename', models.CharField(max_length=255)),
                ('default_credit', models.IntegerField()),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leavemanagement.userdetails')),
            ],
        ),
    ]
