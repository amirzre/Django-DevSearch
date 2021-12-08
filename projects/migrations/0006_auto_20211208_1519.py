# Generated by Django 3.2.9 on 2021-12-08 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211202_1856'),
        ('projects', '0005_auto_20211207_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-voteRatio', '-voteTotal', 'title')},
        ),
        migrations.AlterField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
