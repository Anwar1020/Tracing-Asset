# Generated by Django 4.2.1 on 2024-03-16 10:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('serial_number', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_management.company')),
            ],
        ),
        migrations.CreateModel(
            name='AssetLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_out_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('checked_in_date', models.DateTimeField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_management.asset')),
                ('checked_in_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checked_in_by', to='Asset_management.employee')),
                ('checked_out_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checked_out_by', to='Asset_management.employee')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Asset_management.employee'),
        ),
        migrations.AddField(
            model_name='asset',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_management.company'),
        ),
    ]
