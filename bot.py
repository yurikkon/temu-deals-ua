#!/usr/bin/env python3
"""
Temu Deals Aggregator Bot for Telegram
Automatically finds and posts best deals from Temu to Telegram channel
"""

import os
import re
import json
import time
import logging
import asyncio
from datetime import datetime
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup
from telegram import Bot
from telegram.error import TelegramError
import hashlib

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Temu categories to scrape
CATEGORIES = [
    {'name': 'Электроника', 'url': 'https://www.temu.com/ua/electronics.html'},
    {'name': 'Одежда', 'url': 'https://www.temu.com/ua/womens-fashion.html'},
    {'name': 'Дом и сад', 'url': 'https://www.temu.com/ua/home-garden.html'},
    {'name': 'Красота', 'url': 'https://www.temu.com/ua/beauty-health.html'},
    {'name': 'Спорт', 'url': 'https://www.temu.com/ua/sports-outdoors.html'},
    {'name': 'Детские товары', 'url': 'https://www.temu.com/ua/mother-baby.html'},
]

# Post templates
DEAL_TEMPLATE = """
🔥 <b>{title}</b>

💰 <s>{old_price}</s> → <b>{price}</b> ({discount}%)

📦 <b>Доставка:</b> {shipping}
⭐ <b>Рейтинг:</b> {rating} ({sales} продаж)

🔗 <a href="{affiliate_link}">Купить на Temu</a>

#топ #скидка #товар #покупки
"""

POSTED_DEALS_FILE = 'posted_deals.json'

class TemuDealsBot:
    def __init__(self, token: str, channel_id: str, temu_affiliate_code: str):
        self.token = token
        self.channel_id = channel_id
        self.temu_affiliate_code = temu_affiliate_code
        self.bot = Bot(token=token)
        self.posted_deals = self.load_posted_deals()
        
    def load_posted_deals(self) -> set:
        """Load set of already posted deal IDs"""
        if os.path.exists(POSTED_DEALS_FILE):
            try:
                with open(POSTED_DEALS_FILE, 'r') as f:
                    data = json.load(f)
                    return set(data.get('ids', []))
            except:
                return set()
        return set()
    
    def save_posted_deals(self):
        """Save posted deal IDs"""
        with open(POSTED_DEALS_FILE, 'w') as f:
            json.dump({'ids': list(self.posted_deals)}, f)
    
    def generate_deal_id(self, title: str, price: str) -> str:
        """Generate unique ID for a deal"""
        return hashlib.md5(f"{title}:{price}".encode()).hexdigest()[:12]
    
    def get_affiliate_link(self, product_url: str) -> str:
        """Convert regular URL to affiliate link"""
        # Temu affiliate links format
        if '?' in product_url:
            return f"{product_url}&_r={self.temu_affiliate_code}"
        return f"{product_url}?_r={self.temu_affiliate_code}"
    
    async def parse_temu_deals(self) -> List[Dict]:
        """Parse deals from Temu (simplified - returns sample deals for demo)"""
        # Note: In production, you'd need to handle Temu's anti-scraping
        # For now, return sample deals structure
        
        sample_deals = [
            {
                'title': 'Беспроводные наушники с шумоподавлением',
                'old_price': '$49.99',
                'price': '$19.99',
                'discount': 60,
                'shipping': 'Бесплатно',
                'rating': 4.8,
                'sales': 5000,
                'url': 'https://www.temu.com/ua/headphones',
                'category': 'Электроника'
            },
            {
                'title': 'Умные часы с пульсометром',
                'old_price': '$79.99',
                'price': '$29.99',
                'discount': 63,
                'shipping': 'Бесплатно',
                'rating': 4.7,
                'sales': 3200,
                'url': 'https://www.temu.com/ua/smartwatch',
                'category': 'Электроника'
            },
            {
                'title': 'Набор посуды 12 предметов',
                'old_price': '$59.99',
                'price': '$24.99',
                'discount': 58,
                'shipping': 'Бесплатно',
                'rating': 4.6,
                'sales': 8900,
                'url': 'https://www.temu.com/ua/cookware',
                'category': 'Дом и сад'
            },
            {
                'title': 'Увлажнитель воздуха арома',
                'old_price': '$34.99',
                'price': '$14.99',
                'discount': 57,
                'shipping': 'Бесплатно',
                'rating': 4.9,
                'sales': 12000,
                'url': 'https://www.temu.com/ua/humidifier',
                'category': 'Дом и сад'
            },
            {
                'title': 'Спортивный костюм Oversize',
                'old_price': '$44.99',
                'price': '$19.99',
                'discount': 56,
                'shipping': 'Бесплатно',
                'rating': 4.5,
                'sales': 6700,
                'url': 'https://www.temu.com/ua/sportswear',
                'category': 'Одежда'
            },
            {
                'title': 'Корейская косметика набор',
                'old_price': '$39.99',
                'price': '$15.99',
                'discount': 60,
                'shipping': 'Бесплатно',
                'rating': 4.8,
                'sales': 4500,
                'url': 'https://www.temu.com/ua/skincare',
                'category': 'Красота'
            },
        ]
        
        return sample_deals
    
    def format_deal_message(self, deal: Dict) -> str:
        """Format a deal into a Telegram message"""
        return DEAL_TEMPLATE.format(
            title=deal['title'],
            old_price=deal['old_price'],
            price=deal['price'],
            discount=deal['discount'],
            shipping=deal['shipping'],
            rating=deal['rating'],
            sales=deal['sales'],
            affiliate_link=self.get_affiliate_link(deal['url'])
        )
    
    async def post_deal(self, deal: Dict) -> bool:
        """Post a single deal to the channel"""
        deal_id = self.generate_deal_id(deal['title'], deal['price'])
        
        if deal_id in self.posted_deals:
            logger.info(f"Deal already posted: {deal['title'][:50]}...")
            return False
        
        try:
            message = self.format_deal_message(deal)
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=message,
                parse_mode='HTML',
                disable_web_page_preview=False
            )
            
            self.posted_deals.add(deal_id)
            self.save_posted_deals()
            
            logger.info(f"Posted deal: {deal['title'][:50]}...")
            return True
            
        except TelegramError as e:
            logger.error(f"Error posting deal: {e}")
            return False
    
    async def post_deals_batch(self, max_deals: int = 5):
        """Post a batch of deals to the channel"""
        deals = await self.parse_temu_deals()
        posted_count = 0
        
        for deal in deals[:max_deals]:
            if await self.post_deal(deal):
                posted_count += 1
                # Delay between posts to avoid rate limits
                await asyncio.sleep(2)
        
        logger.info(f"Posted {posted_count} deals")
        return posted_count
    
    async def test_connection(self) -> bool:
        """Test bot connection"""
        try:
            me = await self.bot.get_me()
            logger.info(f"Bot connected: @{me.username}")
            return True
        except Exception as e:
            logger.error(f"Connection test failed: {e}")
            return False


async def main():
    """Main function to run the bot"""
    # Load environment variables
    TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN', '')
    CHANNEL_ID = os.environ.get('CHANNEL_ID', '')
    TEMU_AFFILIATE_CODE = os.environ.get('TEMU_AFFILIATE_CODE', '')
    
    if not all([TELEGRAM_TOKEN, CHANNEL_ID, TEMU_AFFILIATE_CODE]):
        logger.error("Missing environment variables!")
        logger.info("Required: TELEGRAM_TOKEN, CHANNEL_ID, TEMU_AFFILIATE_CODE")
        return
    
    # Initialize bot
    bot = TemuDealsBot(
        token=TELEGRAM_TOKEN,
        channel_id=CHANNEL_ID,
        temu_affiliate_code=TEMU_AFFILIATE_CODE
    )
    
    # Test connection
    if not await bot.test_connection():
        logger.error("Failed to connect to Telegram")
        return
    
    logger.info("Temu Deals Bot started!")
    
    # Post initial batch of deals
    await bot.post_deals_batch(max_deals=5)
    
    logger.info("Initial posting complete!")
    logger.info("Set up cron job or scheduler for regular posting")


if __name__ == '__main__':
    asyncio.run(main())
