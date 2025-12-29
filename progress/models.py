from django.db import models

from users.models import User


class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='userprogress')
    level = models.IntegerField('уровень', default=0)
    current_xp = models.IntegerField('текущий XP', default=0)

    def __str__(self):
        return f'{self.user}: {self.level} - {self.current_xp}'

    class Meta:
        verbose_name = 'Прогресс пользователя'
        verbose_name_plural = 'Прогресс пользователей'
