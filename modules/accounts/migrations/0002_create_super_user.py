from django.db import migrations
from django.contrib.auth import get_user_model

def create_superuser(apps, schema_editor):
    # Получаем модель пользователя
    User = get_user_model()

    # Параметры для суперпользователя
    superuser_email = 'qwe@qwe.com'
    superuser_password = 'qwe'

    # Проверяем, существует ли суперпользователь с таким email
    if not User.objects.filter(email=superuser_email).exists():
        # Создаем суперпользователя
        User.objects.create_superuser(
            email=superuser_email,
            password=superuser_password
        )

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # Зависимость от последней миграции auth
    ]

    operations = [
        migrations.RunPython(create_superuser),  # Запускаем функцию создания суперпользователя
    ]
