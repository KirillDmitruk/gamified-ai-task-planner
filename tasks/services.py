from tasks.models import Task


def create_task(*, title: str, description: str | None = None, user: None) -> Task:
    # Логика создание задачи
    # Смена статуса на 'in_progress'
    # Сохранение в бд
    return Task.objects.create(title=title, description=description, user=user)


def complete_task():
    # Логика завершения задачи
    # Смена статуса на 'done'
    pass
