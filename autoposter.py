#!/usr/bin/env python3
"""
Temu Deals Auto-Poster Bot - Simplified Version
Автоматический постинг скидок в Telegram
Бесплатный хостинг: Render.com, Cyclic.sh, PythonAnywhere
"""

import os
import json
import time
import logging
import random
from datetime import datetime, timedelta
from typing import List, Dict
from telegram import Bot
from telegram.error import TelegramError
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

# Конфигурация из переменных окружения
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', 'YOUR_TOKEN_HERE')
CHANNEL_ID = os.environ.get('CHANNEL_ID', '@temu_skidki_ua')
TEMU_AFFILIATE_CODE = os.environ.get('TEMU_AFFILIATE_CODE', 'affiliate123')
POSTING_TIMES = os.environ.get('POSTING_TIMES', '09:00,12:00,15:00,18:00,21:00').split(',')

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# База сделок для ротации
DEALS_DATABASE = [
    {
        'title': '🔥 Беспроводные наушники Bluetooth 5.3',
        'price': '$19.99',
        'old_price': '$49.99',
        'discount': '60%',
        'category': 'Электроника',
        'icon': '🔌',
        'url': 'electronics/headphones'
    },
    {
        'title': '🔥 Умные часы Smart Watch GT5',
        'price': '$29.99',
        'old_price': '$79.99',
        'discount': '63%',
        'category': 'Электроника',
        'icon': '⌚',
        'url': 'electronics/smartwatch'
    },
    {
        'title': '🔥 Набор посуды 12 предметов',
        'price': '$24.99',
        'old_price': '$59.99',
        'discount': '58%',
        'category': 'Дом',
        'icon': '🍳',
        'url': 'home/cookware'
    },
    {
        'title': '🔥 Увлажнитель воздуха арома',
        'price': '$14.99',
        'old_price': '$34.99',
        'discount': '57%',
        'category': 'Дом',
        'icon': '💨',
        'url': 'home/humidifier'
    },
    {
        'title': '🔥 Спортивный костюм Oversize',
        'price': '$19.99',
        'old_price': '$44.99',
        'discount': '56%',
        'category': 'Одежда',
        'icon': '👕',
        'url': 'fashion/sportswear'
    },
    {
        'title': '🔥 Набор для маникюра 48 предметов',
        'price': '$12.99',
        'old_price': '$29.99',
        'discount': '57%',
        'category': 'Красота',
        'icon': '💅',
        'url': 'beauty/manicure'
    },
    {
        'title': '🔥 Фитнес браслет с пульсометром',
        'price': '$15.99',
        'old_price': '$39.99',
        'discount': '60%',
        'category': 'Спорт',
        'icon': '💪',
        'url': 'sports/fitness'
    },
    {
        'title': '🔥 Детский конструктор 1000 деталей',
        'price': '$19.99',
        'old_price': '$49.99',
        'discount': '60%',
        'category': 'Детское',
        'icon': '🧱',
        'url': 'baby/toys'
    },
    {
        'title': '🔥 Портативная колонка Bluetooth',
        'price': '$16.99',
        'old_price': '$39.99',
        'discount': '58%',
        'category': 'Электроника',
        'icon': '🔊',
        'url': 'electronics/speaker'
    },
    {
        'title': '🔥 Корейская косметика набор',
        'price': '$15.99',
        'old_price': '$39.99',
        'discount': '60%',
        'category': 'Красота',
        'icon': '💄',
        'url': 'beauty/skincare'
    },
]

# Отслеживание опубликованных
POSTED_FILE = 'posted_deals.json'

def load_posted():
    """Загрузка списка опубликованных"""
    if os.path.exists(POSTED_FILE):
        try:
            with open(POSTED_FILE, 'r') as f:
                return set(json.load(f).get('ids', []))
        except:
            return set()
    return set()

def save_posted(posted_ids):
    """Сохранение списка опубликованных"""
    with open(POSTED_FILE, 'w') as f:
        json.dump({'ids': list(posted_ids)}, f)

def get_affiliate_url(url_path):
    """Генерация партнёрской ссылки"""
    return f'https://www.temu.com/ua/{url_path}?_r={TEMU_AFFILIATE_CODE}'

def format_message(deal: Dict, is_premium: bool = False) -> str:
    """Форматирование сообщения"""
    link = get_affiliate_url(deal['url'])
    cat = deal['category'].lower()
    
    if is_premium:
        return f"""
🚀 <b>HOT DEAL!</b>

{deal['icon']} <b>{deal['title']}</b>

💰 <s>{deal['old_price']}</s> → <b>{deal['price']}</b>
📉 Скидка: {deal['discount']}
⭐ Хит продаж!

🔗 <a href="{link}">КУПИТЬ НА TEMU</a>

#{cat} #горячаяскидка #топ #скидка #temu
""".strip()
    
    return f"""
🔥 <b>{deal['title']}</b>

💰 <s>{deal['old_price']}</s> → <b>{deal['price']}</b>
📉 Скидка: {deal['discount']}

🔗 <a href="{link}">Купить на Temu</a>

#{cat} #скидка #топ #покупки
""".strip()

async def send_deal(bot: Bot, deal: Dict, is_premium: bool = False) -> bool:
    """Отправка сделки в канал"""
    try:
        message = format_message(deal, is_premium)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message,
            parse_mode='HTML',
            disable_web_page_preview=False
        )
        return True
    except TelegramError as e:
        logger.error(f"Error sending: {e}")
        return False

async def post_round(bot: Bot, count: int = 3):
    """Публикация раунда сделок"""
    global POSTED_IDS
    
    posted = load_posted()
    available = [d for i, d in enumerate(DEALS_DATABASE) if i not in posted]
    
    if not available:
        # Сброс - все сделки опубликованы
        posted = set()
        available = DEALS_DATABASE
        logger.info("All deals posted, resetting...")
    
    # Выбираем случайные
    selected = random.sample(available, min(count, len(available)))
    
    for i, deal in enumerate(selected):
        deal_idx = DEALS_DATABASE.index(deal)
        is_premium = (i == 0)  # Первый - premium
        
        success = await send_deal(bot, deal, is_premium)
        
        if success:
            posted.add(deal_idx)
            save_posted(posted)
            logger.info(f"Posted: {deal['title'][:40]}...")
        
        # Пауза между постами
        time.sleep(3)
    
    return len(selected)

async def main():
    """Главная функция"""
    if TELEGRAM_TOKEN == 'YOUR_TOKEN_HERE':
        logger.error("Please set TELEGRAM_TOKEN environment variable!")
        return
    
    bot = Bot(token=TELEGRAM_TOKEN)
    
    # Проверка подключения
    try:
        me = await bot.get_me()
        logger.info(f"Bot connected: @{me.username}")
    except Exception as e:
        logger.error(f"Connection failed: {e}")
        return
    
    logger.info("Starting AutoPoster...")
    
    async def scheduled_post():
        """Запланированный постинг"""
        logger.info("Scheduled posting round...")
        await post_round(bot, count=3)
    
    # Настройка планировщика
    scheduler = BackgroundScheduler()
    
    for time_str in POSTING_TIMES:
        try:
            hour, minute = map(int, time_str.split(':'))
            scheduler.add_job(
                scheduled_post,
                CronTrigger(hour=hour, minute=minute),
                id=f'post_{time_str}'
            )
            logger.info(f"Scheduled post at {time_str}")
        except:
            pass
    
    scheduler.start()
    
    # Первый раунд через 10 секунд
    scheduler.add_job(scheduled_post, 'date', run_date=datetime.now() + timedelta(seconds=10))
    
    logger.info("AutoPoster is running! Press Ctrl+C to stop.")
    
    try:
        while True:
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        scheduler.shutdown()
        logger.info("AutoPoster stopped")

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
