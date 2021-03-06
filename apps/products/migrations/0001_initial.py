# Generated by Django 3.2.7 on 2022-03-24 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('main_product_image', models.ImageField(upload_to='main_product_image')),
                ('cpu', models.CharField(max_length=255)),
                ('ram', models.CharField(choices=[('2 GB', '2 GB'), ('4 GB', '4 GB'), ('8 GB', '8 GB'), ('12 GB', '12 GB'), ('16 GB', '16 GB'), ('32 GB', '32 GB')], default='4 GB', max_length=250)),
                ('memory', models.CharField(max_length=50)),
                ('type_memory', models.CharField(choices=[('SSD', 'SSD'), ('HDD', 'HDD')], default='HDD', max_length=250)),
                ('video_card', models.CharField(max_length=250)),
                ('screen', models.CharField(max_length=250)),
                ('time_to_work', models.CharField(max_length=250)),
                ('weight', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('old_price', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True, default='2021-01-01 00:00:00')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', models.ImageField(null=True, upload_to='product_image/')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_image', to='products.product')),
            ],
        ),
    ]
