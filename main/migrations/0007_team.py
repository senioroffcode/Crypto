# Generated by Django 4.2.6 on 2023-10-29 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='Team/')),
                ('name', models.CharField(max_length=255)),
                ('hobby', models.TextField()),
                ('you', models.CharField(max_length=25)),
                ('tw', models.CharField(max_length=25)),
                ('fc', models.CharField(max_length=25)),
                ('insta', models.CharField(max_length=25)),
            ],
        ),
    ]