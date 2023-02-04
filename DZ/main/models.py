from django.db import models

# Create your models here.

class Imprisoned(models.Model):
    # photo = models.ImageField
    name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30)
    article = models.CharField('Статья', max_length=30)
    time_start = models.DateTimeField('Начало срока')
    period = models.CharField('Срок', max_length=30)
    block = models.CharField('Номер блока', max_length=30)
    cell = models.CharField('Номер камеры', max_length=30)
    note_about_behavior = models.TextField('Примечание о поведении')

    def __str__(self):
        return f'Заключенный: {self.last_name}'

    class Meta:
        verbose_name = 'Заключенный'
        verbose_name_plural = 'Заключенные'