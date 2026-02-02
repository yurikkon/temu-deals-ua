#!/usr/bin/env python3
"""
Temu Deals Promo Bot - Viral Marketing System
Автоматическая агрессивная реклама без участия
"""

import os
import json
import time
import random
import logging
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from telegram import Bot
from telegram.error import TelegramError
import requests

# Конфигурация
CONFIG = {
    'bot_token': os.environ.get('TELEGRAM_TOKEN', ''),
    'channel_id': os.environ.get('CHANNEL_ID', '@temu_skidki_ua'),
    'temu_affiliate': os.environ.get('TEMU_AFFILIATE_CODE', ''),
    'admin_chat_id': os.environ.get('ADMIN_CHAT_ID', ''),
}

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Промо-шаблоны для вирусного распространения
PROMO_TEMPLATES = {
    'shock': [
        "🔥 ШОК! Скидки на Temu до 90%!",
        "😱 90% скидка на ВСЁ - это реально?",
        "💸 Я экономлю 5000 грн в месяц на покупках",
        "🤯 Как купить iPhone аксессуары за копейки",
    ],
    'curiosity': [
        "Как я экономлю на покупках?",
        "Секрет который знают 10% покупателей",
        "Что не знают о Temu 90% людей",
        "Лайфхак который изменит твои покупки",
    ],
    'urgency': [
        "⚡ Скидки заканчиваются!",
        "⏰ Осталось 24 часа!",
        "🔥 Горячая распродажа - успей!",
        "💥 5 минут - скидка пропадёт!",
    ],
    'social_proof': [
        "50000 украинцев уже экономят так",
        "Моя подруга не верила, теперь сама заказывает",
        "Отзыв: Получил за 2 недели!",
        "Рекомендую: уже 3-й заказ",
    ],
    'benefit': [
        "Экономь до 80% на каждой покупке",
        "Бесплатная доставка от $20",
        "Возврат денег за 90 дней",
        "Качество которое удивляет",
    ]
}

# Тексты для постинга в разные платформы
PLATFORM_TEXTS = {
    'telegram': {
        'channels': [
            "🔥 @temu_skidki_ua - Лучшие скидки на Temu!",
            "👉 Подпишись @temu_skidki_ua и экономь на покупках",
            "💰 Ищешь скидки? Заходи @temu_skidki_ua",
            "🔥HOT DEAL! @temu_skidki_ua",
        ],
        'comment': "Отличная подборка! Больше здесь: @temu_skidki_ua",
    },
    'facebook': {
        'groups': [
            "🔥 Нашел канал с лучшими скидками на Temu - @temu_skidki_ua\n\nЭкономлю уже 80% на каждой покупке! Рекомендую 👍",
            "💸 Делюсь лайфхаком: подпишитесь на @temu_skidki_ua и получайте лучшие акции первыми!\n\nУже проверил - работает!",
            "😱 Скидки до 90% на Temu! Собрал лучшие здесь: @temu_skidki_ua\n\nНе упусти свой шанс сэкономить!",
        ]
    },
    'instagram': {
        'posts': [
            "💰 Экономь на покупках с Temu!\n\nЛучшие скидки @temu_skidki_ua 🔥",
            "🔥 Скидки которые нельзя пропустить\n\n@temu_skidki_ua - твой гид по акциям",
        ],
        'stories': "🔥 Лучшие скидки на Temu: @temu_skidki_ua"
    },
    'twitter': {
        'tweets': [
            "🔥 Скидки до 90% на Temu! @temu_skidki_ua",
            "💸 Экономлю на покупках с этим каналом @temu_skidki_ua",
        ]
    }
}

# Каналы для продвижения (украинские каналы о шопинге)
PROMOTE_CHANNELS = [
    # Каналы о скидках и акциях
    {'username': 'skidki_ua', 'category': 'скидки'},
    {'username': 'aktsii_ua', 'category': 'акции'},
    {'username': 'shopping_ua', 'category': 'шопинг'},
    {'username': 'freeshopping_ua', 'category': 'шопинг'},
    {'username': 'gurt_ua', 'category': 'шопинг'},
    {'username': 'temu_ua', 'category': 'temu'},
    {'username': 'temu_ukraine', 'category': 'temu'},
    {'username': 'temu_ua', 'category': 'temu'},
    {'username': 'promo_ua', 'category': 'скидки'},
    {'username': 'discount_ua', 'category': 'скидки'},
    {'username': 'sale_ua', 'category': 'акции'},
    {'username': 'topshop_ua', 'category': 'шопинг'},
    {'username': 'loot_ua', 'category': 'скидки'},
    {'username': 'halal_ua', 'category': 'скидки'},
    {'username': 'econom_ua', 'category': 'экономия'},
]

class PromoBot:
    """Бот для агрессивного продвижения"""
    
    def __init__(self):
        self.bot = Bot(token=CONFIG['bot_token'])
        self.promoted_channels = set()
        self.last_promo = {}
    
    async def test_connection(self) -> bool:
        """Проверка подключения"""
        try:
            me = await self.bot.get_me()
            logger.info(f"PromoBot connected: @{me.username}")
            return True
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            return False
    
    def get_promo_text(self, template_type: str = 'shock') -> str:
        """Генерация промо-текста"""
        templates = PROMO_TEMPLATES.get(template_type, PROMO_TEMPLATES['shock'])
        text = random.choice(templates)
        return f"{text}\n\n👉 @temu_skidki_ua"
    
    async def send_promo_to_channel(self, channel_username: str) -> bool:
        """Отправка промо-сообщения в канал"""
        try:
            text = random.choice(PLATFORM_TEXTS['telegram']['channels'])
            await self.bot.send_message(
                chat_id=f"@{channel_username}",
                text=text
            )
            logger.info(f"Promo sent to @{channel_username}")
            return True
        except TelegramError as e:
            logger.error(f"Failed to promo @{channel_username}: {e}")
            return False
    
    async def post_viral_content(self, content: Dict) -> bool:
        """Публикация вирусного контента"""
        try:
            message = self._format_viral_post(content)
            await self.bot.send_message(
                chat_id=CONFIG['channel_id'],
                text=message,
                parse_mode='HTML'
            )
            logger.info(f"Viral post published: {content.get('title', 'unknown')}")
            return True
        except TelegramError as e:
            logger.error(f"Failed to post viral content: {e}")
            return False
    
    def _format_viral_post(self, content: Dict) -> str:
        """Форматирование вирусного поста"""
        types = ['shock', 'curiosity', 'urgency', 'social_proof', 'benefit']
        template_type = random.choice(types)
        
        templates = {
            'shock': f"""🔥 <b>{content.get('title', 'ШОК!')}</b>

{content.get('text', 'Скидки до 90% на всё!')}

👉 Подпишись @temu_skidki_ua и узнавай первым!""",
            
            'curiosity': f"""🤔 <b>{content.get('title', 'Интересный факт')}</b>

{content.get('text', 'Узнай как экономить на покупках')}

👉 Все секреты здесь: @temu_skidki_ua""",
            
            'urgency': f"""⚡ <b>{content.get('title', 'ГОРЯЧАЯ АКЦИЯ!')}</b>

{content.get('text', 'Успей купить по лучшей цене!')}

⏰ Спеши @temu_skidki_ua""",
            
            'social_proof': f"""✅ <b>{content.get('title', 'Рекомендация')}</b>

{content.get('text', 'Уже 50000 человек экономят так!')}

👉 Присоединяйся: @temu_skidki_ua""",
            
            'benefit': f"""💰 <b>{content.get('title', 'ЭКОНОМЬ')}</b>

{content.get('text', 'До 80% на каждой покупке')}

🔥 Забирай скидки: @temu_skidki_ua"""
        }
        
        return templates.get(template_type, templates['shock'])
    
    async def run_promo_campaign(self, intensity: str = 'medium'):
        """Запуск рекламной кампании"""
        logger.info(f"Starting promo campaign with intensity: {intensity}")
        
        intensity_settings = {
            'low': {'channels_per_hour': 5, 'posts_per_day': 10},
            'medium': {'channels_per_hour': 15, 'posts_per_day': 30},
            'high': {'channels_per_hour': 30, 'posts_per_day': 60},
        }
        
        settings = intensity_settings.get(intensity, intensity_settings['medium'])
        
        # Продвижение в каналах
        for channel in PROMOTION_STRATEGY:
            if settings['channels_per_hour'] <= 0:
                break
            
            if channel['username'] not in self.promoted_channels:
                success = await self.send_promo_to_channel(channel['username'])
                
                if success:
                    self.promoted_channels.add(channel['username'])
                    settings['channels_per_hour'] -= 1
                
                time.sleep(random.uniform(30, 120))  # Пауза между действиями
        
        logger.info(f"Promo campaign complete. Promoted {len(self.promoted_channels)} channels")
    
    async def create_daily_viral_posts(self) -> List[Dict]:
        """Создание вирусных постов на день"""
        posts = []
        
        for i in range(10):
            post_type = random.choice(['shock', 'curiosity', 'urgency', 'social_proof', 'benefit'])
            
            content = {
                'title': random.choice(PROMO_TEMPLATES[post_type]),
                'text': self._generate_cta(post_type),
                'type': post_type,
                'scheduled_time': f"{9 + i * 2}:00",  # Каждые 2 часа
            }
            
            posts.append(content)
        
        return posts
    
    def _generate_cta(self, post_type: str) -> str:
        """Генерация призыва к действию"""
        ctas = {
            'shock': "Невероятные скидки которые меняют всё!",
            'curiosity': "Узнай как это работает",
            'urgency': "Скидки ограничены - успей!",
            'social_proof': "Уже тысячи экономят так!",
            'benefit': "Твой шанс сэкономить реальные деньги!",
        }
        return ctas.get(post_type, "Проверь сам!")


# Стратегия продвижения
PROMOTION_STRATEGY = [
    # Фаза 1: Комментирование (мягкое)
    {'action': 'comment', 'channels': ['temu_ua', 'skidki_ua', 'shopping_ua']},
    
    # Фаза 2: Кросс-постинг (среднее)
    {'action': 'crosspost', 'channels': ['aktsii_ua', 'promo_ua', 'discount_ua']},
    
    # Фаза 3: Вирусный контент (агрессивное)
    {'action': 'viral', 'channels': ['gurt_ua', 'loot_ua', 'halal_ua']},
]


class ViralityEngine:
    """Движок вирусного распространения"""
    
    def __init__(self, bot: PromoBot):
        self.bot = bot
        self.viral_posts = []
    
    async def generate_viral_post(self) -> str:
        """Генерация вирусного поста"""
        templates = [
            """🔥 <b>ЛУЧШИЕ СКИДКИ ДНЯ!</b>

Отличные предложения на Temu:

🎧 Наушники - $19.99 (-60%)
⌚ Часы - $29.99 (-63%)
🍳 Посуда - $24.99 (-58%)

🔥 Забирай пока не закончились!
@temu_skidki_ua #скидки #temu #акции""",

            """💸 <b>ЭКОНОМЬ БОЛЬШЕ!</b>

Секретная формула скидок:

1. Заходи @temu_skidki_ua
2. Выбирай лучшие акции
3. Экономь до 80%

Просто? Да! Работает? Проверь!
#экономия #покупки #топ""",

            """😱 <b>ПРАВДА О TEMU</b>

Я 3 месяца заказывал и вот что понял:

✅ Скидки РЕАЛЬНЫЕ до 90%
✅ Доставка БЕСПЛАТНАЯ от $20
✅ Возврат ДЕНЕГ если не понравилось

❌ Но нужно знать где искать...

👉 Все секреты: @temu_skidki_ua""",

            """🚀 <b>HOT DEALS!</b>

Топ-5 товаров со скидками:

1. Наушники $19.99 (-60%)
2. Часы $29.99 (-63%)
3. Косметика $15.99 (-60%)
4. Посуда $24.99 (-58%)
5. Фитнес $15.99 (-60%)

🔥 УСПЕЙ КУПИТЬ!
@temu_skidki_ua #горячиескидки""",
        ]
        
        return random.choice(templates)
    
    async def post_viral_sequence(self, channel_id: str):
        """Публикация вирусной последовательности"""
        for i, post in enumerate(self.viral_posts):
            try:
                await self.bot.bot.send_message(
                    chat_id=channel_id,
                    text=post,
                    parse_mode='HTML'
                )
                logger.info(f"Viral post {i+1} sent")
                
                if i < len(self.viral_posts) - 1:
                    time.sleep(180)  # 3 минуты между постами
                    
            except TelegramError as e:
                logger.error(f"Failed viral post {i}: {e}")


async def main():
    """Главная функция"""
    promo = PromoBot()
    
    # Проверка подключения
    if not await promo.test_connection():
        logger.error("Cannot start without connection")
        return
    
    logger.info("🔥 PromoBot started!")
    
    # Запуск вирусных постов
    engine = ViralityEngine(promo)
    
    while True:
        # Генерация и публикация вирусного контента
        viral_post = await engine.generate_viral_post()
        await promo.post_viral_content({'title': 'Daily Viral', 'text': viral_post})
        
        # Ожидание до следующего поста (2 часа)
        await asyncio.sleep(7200)
    
    # Альтернатива: разовая кампания
    # await promo.run_promo_campaign(intensity='medium')


if __name__ == '__main__':
    asyncio.run(main())
