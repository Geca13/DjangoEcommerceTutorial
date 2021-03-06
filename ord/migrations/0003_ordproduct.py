# Generated by Django 3.1 on 2021-10-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ord', '0002_ord'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
