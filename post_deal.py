import os
import asyncio
from telegram import Bot
from temu_products import get_random_product, format_product_message

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHANNEL_ID = os.environ.get('CHANNEL_ID')

async def post_deal():
    """Постить случайный товар в Telegram канал"""
    try:
        # Получить случайный товар
        product = get_random_product()
        
        # Форматировать сообщение
        text = format_product_message(product)
        
        # Отправить в Telegram
        bot = Bot(token=TELEGRAM_TOKEN)
        await bot.send_message(chat_id=CHANNEL_ID, text=text, parse_mode='HTML')
        
        print(f"✅ Posted: {product['title']}")
        print(f"   Category: {product['category']}")
        print(f"   Price: {product['price']} (was {product['old_price']})")
        print(f"   Link: {product['link']}")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(post_deal())
