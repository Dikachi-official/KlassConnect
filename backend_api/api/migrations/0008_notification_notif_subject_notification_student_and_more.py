# Generated by Django 4.2.9 on 2024-02-11 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_student_password'),
        ('API', '0007_remove_notification_notif_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='notif_subject',
            field=models.CharField(max_length=200, null=True, verbose_name='Notification Subject'),
        ),
        migrations.AddField(
            model_name='notification',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.student'),
        ),
        migrations.AddField(
            model_name='notification',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.teacher'),
        ),
    ]
