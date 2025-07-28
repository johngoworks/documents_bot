import os
from pathlib import Path

# Основные настройки
BOT_TOKEN = "your_bot_token_here"
BASE_TEMP_DIR = "/tmp/docbot"
SESSION_LIFETIME_HOURS = 3
CLEANUP_INTERVAL_MINUTES = 30

# Создаем базовую директорию
Path(BASE_TEMP_DIR).mkdir(exist_ok=True)
