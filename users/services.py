from progress.models import UserProgress
from users.models import User


def create_user(username, phone, password=None) -> User:
    """Создание пользователя и его прогресса"""
    user = User.objects.create(username=username, phone=phone, password=password)
    user_progress = UserProgress.objects.create(user=user)
    user_progress.save()
    return user
