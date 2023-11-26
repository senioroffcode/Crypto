# Generated by Django 4.2.6 on 2023-10-29 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='About/')),
                ('text', models.CharField(max_length=155)),
                ('title', models.CharField(max_length=155)),
                ('mouthwatering', models.CharField(max_length=155)),
                ('locked', models.CharField(max_length=155)),
            ],
        ),
        migrations.AlterField(
            model_name='world',
            name='photo',
            field=models.ImageField(upload_to='World/'),
        ),
    ]
