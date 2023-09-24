from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='Полное имя пользователя', max_length=300)
    first_name = models.CharField(verbose_name='Имя пользователя', max_length=100, default=name)
    second_name = models.CharField(verbose_name='Фамилия пользователя', max_length=100, default=name)
    login = models.CharField(verbose_name='Логин', max_length=100)
    password = models.CharField(verbose_name='Пароль', max_length=100)
    email = models.CharField(verbose_name='Почта', max_length=100)

    def __str__(self):
        return self.login


class Products(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=300)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец продукта')

    def __str__(self):
        return self.name


class Tasks(models.Model):
    name = models.CharField(verbose_name='Название урока', max_length=300)
    description = models.TextField(verbose_name='Описание урока')
    link = models.FileField(verbose_name='Ссылка на видео',
                            upload_to='video',
                            validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    long_time = models.PositiveIntegerField(verbose_name='Длительность видео')


class TaskInProduct(models.Model):
    task_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Урок')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')


class TaskUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, verbose_name='Урок')
    is_watched = models.BooleanField(verbose_name='Просмотр')
    last_watched = models.DateTimeField(verbose_name='Дата последнего просмотра')
    sec_watched = models.PositiveIntegerField(verbose_name='Просмотр в секундах')
    all_watched = models.PositiveIntegerField(verbose_name='Суммарное время просмотра')


class ProductUser(models.Model):
    PERMISSION_ = [
        ('w', 'wait'),
        ('p', 'permissoin')
    ]
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Продукт')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    permission = models.CharField(max_length=1, choices=PERMISSION_, default='w', verbose_name='Разрешение')


class Notifications(models.Model):
    user_to = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='От_кого',
                                verbose_name='От кого')
    user_from = models.ForeignKey(User,
                                  on_delete=models.CASCADE,
                                  related_name='Кому',
                                  verbose_name='Кому')
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='Доступ к какому продукту')
