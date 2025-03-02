"""
.env - Содержит секретные ключи. Обязательно добавлять в .gitignore и никогда не коммитить.
.env.example - Пример файла .env - обязательно идет на Github.
"""

from dotenv import load_dotenv
import os

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Тут мы можем вылавливать из переменных окружения ключи к API
