# Generated by Django 4.2.7 on 2024-02-08 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('replies', models.IntegerField(default=0)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.channel')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filepath', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('replies', models.IntegerField(default=0)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.channel')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.thread')),
            ],
        ),
    ]
