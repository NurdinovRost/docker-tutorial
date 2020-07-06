# Generated by Django 3.0.4 on 2020-07-05 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20200702_1729'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otchet',
            options={'verbose_name': 'Отчет об уборке', 'verbose_name_plural': 'Отчеты об уборке'},
        ),
        migrations.AlterField(
            model_name='otchet',
            name='day_of_week',
            field=models.CharField(choices=[('Пон', 'Понедельник'), ('Вт', 'Вторник'), ('Ср', 'Среда'), ('Чт', 'Четверг'), ('Пт', 'Пятница'), ('Сб', 'Суббота'), ('Вс', 'Воскресенье')], max_length=20, verbose_name='День недели'),
        ),
        migrations.AlterField(
            model_name='otchet',
            name='status',
            field=models.CharField(choices=[('Ок', 'Проведена'), ('Пр', 'Есть проблемы')], max_length=20, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_worker',
            field=models.BooleanField(null=True, verbose_name='Является уборщиком'),
        ),
    ]
