import os
from pathlib import Path

# Основные настройки
BOT_TOKEN = "8338587060:AAEeIEvZrGBjwglgK48m0TeLIj02_eXxfcA"
BASE_TEMP_DIR = "/tmp/docbot"
SESSION_LIFETIME_HOURS = 3
CLEANUP_INTERVAL_MINUTES = 30

# Создаем базовую директорию
Path(BASE_TEMP_DIR).mkdir(exist_ok=True)
