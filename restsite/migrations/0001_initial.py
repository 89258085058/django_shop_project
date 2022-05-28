# Generated by Django 4.0.4 on 2022-05-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Название')),
                ('descriptions', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='images', verbose_name='изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена')),
                ('type', models.CharField(choices=[('BRK', 'завтрак'), ('LUN', 'обед'), ('DIN', 'ужин')], default='BRK', max_length=3, verbose_name='Тип')),
            ],
        ),
    ]
