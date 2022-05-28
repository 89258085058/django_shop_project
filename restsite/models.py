from django.db import models

class ItemModel(models.Model):
    title = models.CharField(max_length=70, verbose_name="Название")
    descriptions = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="images", verbose_name="изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    TYPE = [
        ('BRK', 'завтрак'),
        ('LUN', 'обед'),
        ('DIN', 'ужин'),
    ]
    type = models.CharField(choices=
                            TYPE, max_length=3, default='BRK', verbose_name='Тип')

    def __str__(self):
        return self.title

class TestModel(models.Model):
    title = models.CharField(max_length=10, default=100)
    column1 = models.CharField(max_length=10, default=100)
    column2 = models.CharField(max_length=10, default=100)
    column3 = models.CharField(max_length=10, default=100)

