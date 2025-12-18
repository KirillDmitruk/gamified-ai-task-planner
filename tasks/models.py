from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Task(models.Model):
    STATUS_NOT_STARTED = 'not_started'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_DONE = 'done'
    STATUS = [
        (STATUS_NOT_STARTED, 'Не приступал к выполнению'),
        (STATUS_IN_PROGRESS, 'В процессе выполнения'),
        (STATUS_DONE, 'Выполнено'),
    ]
    title = models.CharField('название', max_length=100)
    description = models.TextField('описание', max_length=500, **NULLABLE)
    status = models.CharField('Статус', max_length=20, choices=STATUS, default=STATUS_NOT_STARTED)
    created_at = models.DateField('дата начала', auto_now_add=True)
    end_date = models.DateField('дата окончания', **NULLABLE)

    def __str__(self):
        return f'{self.title}: {self.status}'

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class SubTask(models.Model):
    STATUS_NOT_STARTED = 'not_started'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_DONE = 'done'
    STATUS = [
        (STATUS_NOT_STARTED, 'Не приступал к выполнению'),
        (STATUS_IN_PROGRESS, 'В процессе выполнения'),
        (STATUS_DONE, 'Выполнено'),
    ]
    task = models.ForeignKey('Task', on_delete=models.CASCADE, **NULLABLE, related_name='подзадача')
    title = models.CharField('название', max_length=100)
    status = models.CharField('cтатус', max_length=20, choices=STATUS, default=STATUS_NOT_STARTED)
    created_at = models.DateField('дата создания', auto_now_add=True)

    def __str__(self):
        return f'{self.title}: {self.status}'

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'
