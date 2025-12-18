from django.contrib.auth.models import AbstractUser
from django.db import models

from tasks.models import NULLABLE


class User(AbstractUser):
    username = models.CharField('имя пользователя', max_length=150, unique=True)

    phone = models.CharField('телефон', max_length=35, unique=True, **NULLABLE)
    avatar = models.ImageField('аватар', upload_to='users/', **NULLABLE)
    level = models.IntegerField('уровень', default=0)
    current_xp = models.IntegerField('текущий XP', default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
