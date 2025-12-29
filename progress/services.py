from progress.models import UserProgress
from users.models import User


def add_xp(user: User, amount_xp: int):
    """
    Начисление XP пользователю.
    Создаёт UserProgress, если по какой-то причине его нет.
    """
    user_progress, _ = UserProgress.objects.get_or_create(user=user)
    user_progress.current_xp += amount_xp
    print(f'Прибавили xp')
    print(user_progress.current_xp)

    # Проверка на повышен уровня
    if user_progress.current_xp >= user_progress.xp_for_next_lvl:
        print(f'Текущее хр: {user_progress.current_xp}')
        user_progress.current_xp -= user_progress.xp_for_next_lvl
        user_progress.level += 1
        print(f'Уровень увеличен, текуший ур: {user_progress.level}')
        # TODO: Добавить логику увеличения требуемого xp для след уровня на 10-20%
    user_progress.save()
