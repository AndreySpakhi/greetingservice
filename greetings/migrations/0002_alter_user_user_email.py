# Generated by Django 4.0.1 on 2022-01-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.CharField(db_index=True, max_length=50, verbose_name='Фамилия пользователя'),
        ),
    ]
