# Generated by Django 5.2.2 on 2025-06-11 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='products.category')),
            ],
            options={
                'unique_together': {('category', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('distance', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('brand', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.subcategory')),
            ],
        ),
    ]
