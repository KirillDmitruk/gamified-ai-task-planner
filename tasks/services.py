from progress.services import add_xp
from tasks.models import Task, TaskStatus
from users.models import User


def create_task(*, title: str, description: str | None = None, user: User | None) -> Task:
    """Создание задачи и сохранение в бд"""
    return Task.objects.create(title=title, description=description, user=user)


def complete_task(task):
    """Завершение задачи и смена статуса на 'done'"""
    task.status = TaskStatus.DONE
    task.save()
    add_xp(task.user, 10)
    # TODO: Проверить через shell начисление хр

