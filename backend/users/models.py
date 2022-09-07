from api import conf

from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, CheckConstraint, EmailField,
                              ManyToManyField, Q)
from django.db.models.functions import Length
from django.utils.translation import gettext_lazy as _

from .validators import MinLenValidator, OneOfTwoValidator

CharField.register_lookup(Length)


class MyUser(AbstractUser):

    email = EmailField(
        verbose_name='email',
        max_length=50,
        unique=True,
        help_text='Обязательно. До 50 символов.'
    )
    username = CharField(
        verbose_name='Никнейм',
        max_length=100,
        unique=True,
        help_text='Обязательно. 3-100 символов.',
        validators=(
            MinLenValidator(min_len=3),
            OneOfTwoValidator(),
        ),
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=100,
        help_text='Обязательно. До 100 символов.'
    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=50,
        help_text='Обязательно. 3-100 символов.'
    )
    password = CharField(
        verbose_name=_('Пароль'),
        max_length=30,
        help_text='Обязательно. До 30 символов'
    )
    subscribe = ManyToManyField(
        verbose_name='Подписка',
        verbose_name_plural='Подписки',
        related_name='subscribers',
        to='self',
        symmetrical=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)
        constraints = (
            CheckConstraint(
                check=Q(username__length__gte=3),
                name='\nusername too short\n',
            ),
        )

    def __str__(self):
        return f'{self.username}: {self.email}'
