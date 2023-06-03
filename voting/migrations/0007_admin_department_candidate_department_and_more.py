# Generated by Django 4.1.7 on 2023-06-02 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_college_department_delete_election_admin_otp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.department'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.department'),
        ),
        migrations.AddField(
            model_name='position',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.department'),
        ),
        migrations.AddField(
            model_name='voter',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.department'),
        ),
        migrations.AddField(
            model_name='votes',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.department'),
        ),
    ]