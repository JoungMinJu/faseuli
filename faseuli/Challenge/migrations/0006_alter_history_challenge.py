# Generated by Django 3.2.3 on 2021-09-25 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Challenge', '0005_alter_history_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='Challenge.challenge'),
        ),
    ]
