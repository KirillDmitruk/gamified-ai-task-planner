from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class TaskStatus(models.TextChoices):
    IN_PROGRESS = 'in_progress', 'В процессе'
    DONE = 'done', 'Выполнено'


class Task(models.Model):
    title = models.CharField('название', max_length=100)
    description = models.TextField('описание', max_length=500, **NULLABLE)
    status = models.CharField('Статус', max_length=20, choices=TaskStatus.choices, default=TaskStatus.IN_PROGRESS)
    created_at = models.DateTimeField('дата начала', auto_now_add=True)
    end_date = models.DateTimeField('дата окончания', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return f'{self.title}: {self.status}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class SubTask(models.Model):
    task = models.ForeignKey('Task', on_delete=models.CASCADE, **NULLABLE, related_name='подзадача')
    title = models.CharField('название', max_length=100)
    status = models.CharField('cтатус', max_length=20, choices=TaskStatus.choices, default=TaskStatus.IN_PROGRESS)
    created_at = models.DateTimeField('дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.status}'

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'
