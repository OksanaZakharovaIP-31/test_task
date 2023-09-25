# Generated by Django 4.2.5 on 2023-09-25 08:02

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Полное имя пользователя')),
                ('first_name', models.CharField(default=models.CharField(max_length=300, verbose_name='Полное имя пользователя'), max_length=100, verbose_name='Имя пользователя')),
                ('second_name', models.CharField(default=models.CharField(max_length=300, verbose_name='Полное имя пользователя'), max_length=100, verbose_name='Фамилия пользователя')),
                ('login', models.CharField(max_length=100, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название продукта')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.person', verbose_name='Владелец продукта')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название урока')),
                ('description', models.TextField(verbose_name='Описание урока')),
                ('link', models.FileField(upload_to='video', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])], verbose_name='Ссылка на видео')),
                ('long_time', models.PositiveIntegerField(verbose_name='Длительность видео')),
            ],
        ),
        migrations.CreateModel(
            name='TaskUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_watched', models.BooleanField(verbose_name='Просмотр')),
                ('last_watched', models.DateTimeField(verbose_name='Дата последнего просмотра')),
                ('sec_watched', models.PositiveIntegerField(verbose_name='Просмотр в секундах')),
                ('all_watched', models.PositiveIntegerField(verbose_name='Суммарное время просмотра')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasks', verbose_name='Урок')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.person', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='TaskInProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.products', verbose_name='Продукт')),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.person', verbose_name='Урок')),
            ],
        ),
        migrations.CreateModel(
            name='ProductUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('w', 'wait'), ('p', 'permissoin')], default='w', max_length=1, verbose_name='Разрешение')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.products', verbose_name='Продукт')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.person', verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.products', verbose_name='Доступ к какому продукту')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Кому', to='tasks.person', verbose_name='Кому')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='От_кого', to='tasks.person', verbose_name='От кого')),
            ],
        ),
    ]