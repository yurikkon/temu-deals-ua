#!/bin/bash

# 🚀 Быстрый запуск Temu Deals Bot
# Скопируй этот файл как start.sh и запусти: bash start.sh

echo "🚀 Запуск Temu Deals Bot..."

# Проверка Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python не найден! Установите Python 3.8+"
    exit 1
fi

# Установка зависимостей
echo "📦 Установка зависимостей..."
pip install -r requirements.txt

# Проверка конфигурации
if [ ! -f .env ]; then
    echo "📝 Создание .env файла..."
    cat > .env << 'EOF'
# Заполни свои данные:
TELEGRAM_TOKEN=YOUR_BOT_TOKEN_HERE
CHANNEL_ID=@temu_skidki_ua
TEMU_AFFILIATE_CODE=your_affiliate_code
POSTING_TIMES=09:00,12:00,15:00,18:00,21:00
EOF
    echo "✅ Файл .env создан!"
    echo "⚠️  ОТРЕДАКТИРУЙ .env файл и добавь свои данные!"
fi

# Запуск
echo "🎯 Запуск бота..."
python3 autoposter.py

echo "✅ Бот запущен!"
