FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование файлов
COPY *.py .
COPY *.md .

# Переменные окружения
ENV TELEGRAM_TOKEN=${TELEGRAM_TOKEN}
ENV CHANNEL_ID=${CHANNEL_ID}
ENV TEMU_AFFILIATE_CODE=${TEMU_AFFILIATE_CODE}
ENV POSTING_TIMES=09:00,12:00,15:00,18:00,21:00

# Запуск
CMD ["python", "autoposter.py"]
