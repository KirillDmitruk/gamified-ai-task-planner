from django.conf import settings
from django.db import models


class UserProgress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress')
    level = models.IntegerField('уровень', default=0)
    current_xp = models.IntegerField('текущий XP', default=0)
    xp_for_next_lvl = models.IntegerField('XP для следующего уровня', default=100)

    def __str__(self):
        return f'{self.user.username} - Уровень {self.level}, XP {self.current_xp}'

    class Meta:
        verbose_name = 'Прогресс пользователя'
        verbose_name_plural = 'Прогресс пользователей'
