# Generated by Django 4.0.1 on 2022-03-06 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securidocs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=15)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('new_password', models.CharField(max_length=8)),
                ('confirm_password', models.CharField(max_length=8)),
            ],
        ),
        migrations.RemoveField(
            model_name='login',
            name='name',
        ),
        migrations.RemoveField(
            model_name='login',
            name='phone',
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=8),
        ),
    ]