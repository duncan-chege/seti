# Generated by Django 2.1.7 on 2019-03-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snitch', '0009_auto_20190329_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pics/'),
        ),
    ]