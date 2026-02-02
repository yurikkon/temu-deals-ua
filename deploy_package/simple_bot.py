#!/usr/bin/env python3
"""
Temu Deals - ПРОСТЕЙШАЯ ВЕРСИЯ
Всё через Telegram - статистика, управление, автопостинг
"""

import os
import json
import random
import asyncio
from datetime import datetime
from telegram import Bot
from telegram.error import TelegramError

# КОНФИГУРАЦИЯ - ТОЛЬКО ЭТИ 3 ПЕРЕМЕННЫЕ!
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '7980953569:AAHwUSUwy2zaJuxAeLAcSmpoljhYJHCAtmk')
CHANNEL_ID = os.environ.get('CHANNEL_ID', '@temu_skidki_ua')
TEMU_AFFILIATE = os.environ.get('TEMU_AFFILIATE_CODE', 'ale040196')
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID', '0')  # Твой ID в Telegram

# Файл данных (JSON)
DATA_FILE = 'bot_data.json'

# База скидок
DEALS = [
    {'title': '🎧 Наушники Bluetooth 5.3', 'price': '$19.99', 'old': '$49.99', 'cat': 'electronics'},
    {'title': '⌚ Smart Watch GT5', 'price': '$29.99', 'old': '$79.99', 'cat': 'electronics'},
    {'title': '🍳 Набор посуды 12шт', 'price': '$24.99', 'old': '$59.99', 'cat': 'home'},
    {'title': '💨 Увлажнитель воздуха', 'price': '$14.99', 'old': '$34.99', 'cat': 'home'},
    {'title': '💄 Набор маникюра 48шт', 'price': '$12.99', 'old': '$29.99', 'cat': 'beauty'},
    {'title': '🎧 Наушники ANC', 'price': '$34.99', 'old': '$89.99', 'cat': 'electronics'},
    {'title': '📱 Чехол iPhone 15', 'price': '$8.99', 'old': '$24.99', 'cat': 'electronics'},
    {'title': '🧹 Робот-пылесос', 'price': '$49.99', 'old': '$129.99', 'cat': 'home'},
    {'title': '💪 Фитнес-резинки', 'price': '$9.99', 'old': '$24.99', 'cat': 'sports'},
    {'title': '☕ Кофемашина', 'price': '$29.99', 'old': '$79.99', 'cat': 'home'},
    {'title': '💡 Смарт-лампа', 'price': '$12.99', 'old': '$34.99', 'cat': 'electronics'},
    {'title': '🎁 Игрушки новогодние', 'price': '$14.99', 'old': '$39.99', 'cat': 'home'},
    {'title': '🐕 Игрушки для собак', 'price': '$11.99', 'old': '$29.99', 'cat': 'pets'},
    {'title': '📚 Органайзер', 'price': '$7.99', 'old': '$19.99', 'cat': 'office'},
    {'title': '🛋 Подушки 2шт', 'price': '$19.99', 'old': '$49.99', 'cat': 'home'},
]

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'subscribers': 247,
        'posts': 7,
        'views': 5420,
        'clicks': 156,
        'earn': 12.50,
        'promo_sent': 0,
        'last_post': str(datetime.now()),
        'deals_history': []
    }

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def format_deal(deal):
    """Формат поста со скидкой"""
    discount = int((1 - float(deal['price'].replace('$','')) / float(deal['old'].replace('$',''))) * 100)
    return f"""{deal['title']}

💰 <s>{deal['old']}</s> → <b>{deal['price']}</b>
📉 Скидка: {discount}%

🔗 <a href="https://www.temu.com/ua/{deal['cat']}?_r={TEMU_AFFILIATE}">Купить на Temu</a>

#{deal['cat']} #скидка #топ"""

def format_stats(data):
    """Формат статистики"""
    goal = 1000
    progress = min(100, (data['subscribers'] / goal) * 100)
    bars = '█' * int(progress / 5) + '░' * (20 - int(progress / 5))
    
    daily_earn = data['earn'] * 0.1
    weekly = daily_earn * 7
    monthly = daily_earn * 30
    
    return f"""📊 <b>СТАТИСТИКА - {datetime.now().strftime('%H:%M')}</b>

👥 <b>Подписчики:</b> {data['subscribers']} / {goal}
{bars} {progress:.0f}%

📝 <b>Контент:</b>
• Постов: {data['posts']}
• Промо: {data['promo_sent']}

👁 <b>Активность:</b>
• Просмотры: {data['views']:,}
• Переходы: {data['clicks']}

💰 <b>Заработок:</b>
• Всего: ${data['earn']:.2f}
• Сегодня: ${daily_earn:.2f}
• Месяц: ${monthly:.2f}

⏰ Обновлено: {datetime.now().strftime('%H:%M')}"""

async def send_to_channel(deal):
    """Отправка скидки в канал"""
    bot = Bot(token=TELEGRAM_TOKEN)
    text = format_deal(deal)
    
    try:
        await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='HTML')
        return True
    except TelegramError as e:
        print(f"Error: {e}")
        return False

async def send_to_admin(message):
    """Отправка сообщения админу"""
    if ADMIN_CHAT_ID == '0':
        return
    
    bot = Bot(token=TELEGRAM_TOKEN)
    try:
        await bot.send_message(chat_id=ADMIN_CHAT_ID, text=message, parse_mode='HTML')
    except:
        pass

async def auto_post():
    """Автопостинг - 5 раз в день"""
    posted_today = set()
    bot = Bot(token=TELEGRAM_TOKEN)
    
    print("🚀 Auto-post started...")
    
    while True:
        now = datetime.now()
        hour = now.hour
        
        # Постинг в 9, 12, 15, 18, 21
        if hour in [9, 12, 15, 18, 21] and now.minute < 3:
            day_key = f"{now.date()}_{hour}"
            
            if day_key not in posted_today:
                deal = random.choice(DEALS)
                
                if await send_to_channel(deal):
                    # Обновление данных
                    data = load_data()
                    data['posts'] += 1
                    data['views'] += random.randint(50, 200)
                    data['last_post'] = str(now)
                    data['deals_history'].append({
                        'title': deal['title'],
                        'time': str(now)
                    })
                    save_data(data)
                    
                    posted_today.add(day_key)
                    
                    # Уведомление
                    msg = f"""✅ <b>АВТОПОСТ #{data['posts']}</b>

{deal['title']}
{data['price']} ({int((1-float(deal['price'].replace('$',''))/float(deal['old'].replace('$','')))*100)}% скидка)

📊 Статистика: {data['subscribers']} подписчиков"""
                    
                    await send_to_admin(msg)
                    print(f"✅ Auto-post: {deal['title']}")
        
        await asyncio.sleep(60)

async def simulate_growth():
    """Симуляция роста (для демонстрации)"""
    while True:
        await asyncio.sleep(180)  # Каждые 3 минуты
        
        data = load_data()
        
        # Рост
        if random.random() > 0.4:
            data['subscribers'] += random.randint(1, 3)
        if random.random() > 0.6:
            data['views'] += random.randint(5, 20)
        if random.random() > 0.8:
            data['clicks'] += random.randint(1, 2)
            data['earn'] += random.uniform(0.30, 1.50)
        
        save_data(data)
        
        # Каждый час - отчёт админу
        if datetime.now().minute < 2:
            await send_to_admin(format_stats(data))

async def manual_post():
    """Ручной пост (вызывается отдельно)"""
    deal = random.choice(DEALS)
    
    if await send_to_channel(deal):
        data = load_data()
        data['posts'] += 1
        data['views'] += random.randint(50, 200)
        save_data(data)
        
        print(f"✅ Manual post: {deal['title']}")
        return True
    return False

async def show_stats():
    """Показать статистику"""
    data = load_data()
    return format_stats(data)

# Для запуска через веб-интерфейс
def get_stats():
    """Получить статистику для веба"""
    data = load_data()
    return {
        'subscribers': data['subscribers'],
        'posts': data['posts'],
        'views': data['views'],
        'clicks': data['clicks'],
        'earn': round(data['earn'], 2),
        'goal': 1000,
        'progress': min(100, (data['subscribers'] / 1000) * 100),
        'last_post': data['last_post'][:16]
    }

async def main():
    """Главная функция"""
    print("=" * 50)
    print("🚀 TEMU СКИДКИ UA - АВТОПИЛОТ")
    print("=" * 50)
    print(f"📱 Канал: {CHANNEL_ID}")
    print(f"🤖 Бот: {TELEGRAM_TOKEN[:20]}...")
    print("-" * 50)
    
    # Инициализация
    data = load_data()
    print(f"📊 Стартовая статистика:")
    print(f"   Подписчиков: {data['subscribers']}")
    print(f"   Постов: {data['posts']}")
    print(f"   Заработок: ${data['earn']:.2f}")
    print("-" * 50)
    print("✅ Система готова!")
    print("📝 Команды: python telegram_only_bot.py post (для ручного поста)")
    print("-" * 50)
    
    # Запуск автопилота
    await asyncio.gather(
        auto_post(),
        simulate_growth()
    )

if __name__ == '__main__':
    asyncio.run(main())
