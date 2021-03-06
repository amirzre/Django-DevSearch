# Generated by Django 3.2.9 on 2021-12-07 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211202_1856'),
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
