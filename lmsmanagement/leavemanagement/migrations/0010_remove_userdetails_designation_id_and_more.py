# Generated by Django 4.2.8 on 2024-01-16 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leavemanagement', '0009_alter_lms_leave_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='designation_id',
        ),
        migrations.AddField(
            model_name='leavetype',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='leavemanagement.userdetails'),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='leavename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='leavetype',
            name='leavetype',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]