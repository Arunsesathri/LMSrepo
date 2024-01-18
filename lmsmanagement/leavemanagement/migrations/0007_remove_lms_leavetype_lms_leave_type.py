# Generated by Django 4.2.8 on 2024-01-16 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leavemanagement', '0006_lms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lms',
            name='leavetype',
        ),
        migrations.AddField(
            model_name='lms',
            name='leave_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leavemanagement.leavetype'),
        ),
    ]