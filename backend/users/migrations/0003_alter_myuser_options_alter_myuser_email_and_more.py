# Generated by Django 4.0.4 on 2022-09-09 19:31

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myuser_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'ordering': ('username',), 'verbose_name': 'Пользователь'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(help_text='Обязательно. До 50 символов.', max_length=50, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(help_text='Обязательно. До 100 символов.', max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(help_text='Обязательно. 3-100 символов.', max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(help_text='Обязательно. До 150 символов', max_length=150, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(help_text='Обязательно. 3-100 символов.', max_length=100, unique=True, validators=[users.validators.MinLenValidator(min_len=3), users.validators.OneOfTwoValidator()], verbose_name='Никнейм'),
        ),
    ]
