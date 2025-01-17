# Generated by Django 5.0.7 on 2024-07-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Enter your email address', max_length=254, unique=True)),
                ('password', models.CharField(help_text='Enter your password', max_length=128)),
                ('check_me_out', models.BooleanField(default=False, help_text='Check this box if you want to be checked out')),
            ],
        ),
    ]
