import os
import random
import asyncio
from telegram import Bot

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')
TEMU_AFFILIATE = os.environ.get('TEMU_AFFILIATE_CODE', 'ale040196')
TEMU_BASE_URL = os.environ.get('TEMU_BASE_URL', 'https://www.temu.com')

# Simulated deals database
DEALS = [
    {
        "title": "🎁 Бесплатная доставка + скидка 100₴",
        "description": "Новая акция от Temu! Получите скидку 100₴ на первый заказ + бесплатная доставка",
        "link": f"{TEMU_BASE_URL}?referral_code={TEMU_AFFILIATE}"
    },
    {
        "title": "🔥 Скидка 50% на электронику",
        "description": "Отличные цены на гаджеты и аксессуары. Успейте заказать!",
        "link": f"{TEMU_BASE_URL}?referral_code={TEMU_AFFILIATE}"
    },
    {
        "title": "🛍️ До -70% на одежду",
        "description": "Новая коллекция летних вещей по супер ценам",
        "link": f"{TEMU_BASE_URL}?referral_code={TEMU_AFFILIATE}"
    },
    {
        "title": "🏠 Товары для дома -60%",
        "description": "Уют и комфорт для вашего дома по отличным ценам",
        "link": f"{TEMU_BASE_URL}?referral_code={TEMU_AFFILIATE}"
    },
    {
        "title": "💄 Красота и уход -50%",
        "description": "Косметика и средства по уходу за собой",
        "link": f"{TEMU_BASE_URL}?referral_code={TEMU_AFFILIATE}"
    }
]

async def post_deal():
    try:
        deal = random.choice(DEALS)
        text = f"""<b>{deal['title']}</b>

{deal['description']}

🔗 <a href="{deal['link']}">Заказать на Temu</a>

#temu #скидки #акции #топпредложения"""
        
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='HTML')
        print(f"✅ Posted: {deal['title']}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(post_deal())
