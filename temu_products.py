"""
Temu Products Database with Real Working Links
Реальные товары с рабочими ссылками на Temu
"""

import os
import random
from datetime import datetime

TEMU_AFFILIATE = os.environ.get('TEMU_AFFILIATE_CODE', 'ale040196')

# Реальные товары с рабочими ссылками на Temu
# Все ссылки ведут на поиск товаров с affiliate кодом
PRODUCTS = [
    # Электроника и гаджеты
    {
        "category": "Электроника",
        "title": "🎧 Беспроводные наушники TWS",
        "description": "Качественные беспроводные наушники с шумоподавлением. Батарея 30+ часов. Скидка 60%!",
        "price": "₴299",
        "old_price": "₴749",
        "link": f"https://www.temu.com/ua/search?q=wireless+earbuds&refer_code={TEMU_AFFILIATE}",
        "emoji": "🎧"
    },
    {
        "category": "Электроника",
        "title": "📱 Защитное стекло для телефона",
        "description": "Закаленное стекло 9H для всех моделей. Легко клеится. Скидка 70%!",
        "price": "₴49",
        "old_price": "₴159",
        "link": f"https://www.temu.com/ua/search?q=tempered+glass&refer_code={TEMU_AFFILIATE}",
        "emoji": "🛡️"
    },
    {
        "category": "Электроника",
        "title": "🔋 Портативное зарядное устройство",
        "description": "Power Bank 20000mAh с быстрой зарядкой. Скидка 50%!",
        "price": "₴199",
        "old_price": "₴399",
        "link": f"https://www.temu.com/ua/search?q=power+bank&refer_code={TEMU_AFFILIATE}",
        "emoji": "⚡"
    },
    
    # Одежда и аксессуары
    {
        "category": "Одежда",
        "title": "👕 Летние футболки (набор 3 шт)",
        "description": "Комфортные хлопковые футболки. Разные цвета. Скидка 65%!",
        "price": "₴149",
        "old_price": "₴429",
        "link": f"https://www.temu.com/ua/search?q=t-shirt+men&refer_code={TEMU_AFFILIATE}",
        "emoji": "👔"
    },
    {
        "category": "Одежда",
        "title": "👟 Спортивные кроссовки",
        "description": "Удобные кроссовки для спорта и прогулок. Скидка 55%!",
        "price": "₴249",
        "old_price": "₴549",
        "link": f"https://www.temu.com/ua/search?q=sports+shoes&refer_code={TEMU_AFFILIATE}",
        "emoji": "🏃"
    },
    {
        "category": "Одежда",
        "title": "🧢 Кепка/Бейсболка",
        "description": "Стильная кепка для защиты от солнца. Скидка 60%!",
        "price": "₴79",
        "old_price": "₴199",
        "link": f"https://www.temu.com/ua/search?q=baseball+cap&refer_code={TEMU_AFFILIATE}",
        "emoji": "🎩"
    },
    
    # Товары для дома
    {
        "category": "Дом",
        "title": "🛏️ Комплект постельного белья",
        "description": "Мягкое постельное белье 4 предмета. Скидка 50%!",
        "price": "₴299",
        "old_price": "₴599",
        "link": f"https://www.temu.com/ua/search?q=bedding+set&refer_code={TEMU_AFFILIATE}",
        "emoji": "🛌"
    },
    {
        "category": "Дом",
        "title": "🎀 Декоративные подушки (2 шт)",
        "description": "Красивые подушки для дивана. Разные узоры. Скидка 55%!",
        "price": "₴129",
        "old_price": "₴289",
        "link": f"https://www.temu.com/ua/search?q=decorative+pillows&refer_code={TEMU_AFFILIATE}",
        "emoji": "🎀"
    },
    {
        "category": "Дом",
        "title": "💡 LED лампочки (4 шт)",
        "description": "Энергосберегающие LED лампы. Скидка 60%!",
        "price": "₴99",
        "old_price": "₴249",
        "link": f"https://www.temu.com/ua/search?q=led+bulbs&refer_code={TEMU_AFFILIATE}",
        "emoji": "💡"
    },
    
    # Красота и уход
    {
        "category": "Красота",
        "title": "💄 Набор косметики (12 предметов)",
        "description": "Полный набор косметики для макияжа. Скидка 65%!",
        "price": "₴179",
        "old_price": "₴509",
        "link": f"https://www.temu.com/ua/search?q=makeup+set&refer_code={TEMU_AFFILIATE}",
        "emoji": "💅"
    },
    {
        "category": "Красота",
        "title": "🧴 Маска для лица (10 шт)",
        "description": "Тканевые маски для лица. Разные типы. Скидка 50%!",
        "price": "₴89",
        "old_price": "₴179",
        "link": f"https://www.temu.com/ua/search?q=face+mask&refer_code={TEMU_AFFILIATE}",
        "emoji": "🧖"
    },
    {
        "category": "Красота",
        "title": "🧴 Набор средств для ухода",
        "description": "Шампунь, кондиционер, маска. Скидка 55%!",
        "price": "₴149",
        "old_price": "₴329",
        "link": f"https://www.temu.com/ua/search?q=hair+care&refer_code={TEMU_AFFILIATE}",
        "emoji": "💆"
    },
    
    # Спорт и фитнес
    {
        "category": "Спорт",
        "title": "💪 Гантели (набор 2 шт)",
        "description": "Регулируемые гантели 2-10 кг. Скидка 50%!",
        "price": "₴249",
        "old_price": "₴499",
        "link": f"https://www.temu.com/ua/search?q=dumbbells&refer_code={TEMU_AFFILIATE}",
        "emoji": "💪"
    },
    {
        "category": "Спорт",
        "title": "🧘 Коврик для йоги",
        "description": "Нескользящий коврик для йоги и фитнеса. Скидка 60%!",
        "price": "₴99",
        "old_price": "₴249",
        "link": f"https://www.temu.com/ua/search?q=yoga+mat&refer_code={TEMU_AFFILIATE}",
        "emoji": "🧘"
    },
    {
        "category": "Спорт",
        "title": "⌚ Фитнес браслет",
        "description": "Умный браслет с пульсометром и шагомером. Скидка 55%!",
        "price": "₴199",
        "old_price": "₴439",
        "link": f"https://www.temu.com/ua/search?q=fitness+tracker&refer_code={TEMU_AFFILIATE}",
        "emoji": "📊"
    },
    
    # Кухня
    {
        "category": "Кухня",
        "title": "🍳 Набор кухонной посуды (10 предметов)",
        "description": "Антипригарная посуда для всех плит. Скидка 50%!",
        "price": "₴349",
        "old_price": "₴699",
        "link": f"https://www.temu.com/ua/search?q=cookware+set&refer_code={TEMU_AFFILIATE}",
        "emoji": "🍽️"
    },
    {
        "category": "Кухня",
        "title": "🔪 Набор ножей (6 предметов)",
        "description": "Острые кухонные ножи из нержавейки. Скидка 55%!",
        "price": "₴129",
        "old_price": "₴289",
        "link": f"https://www.temu.com/ua/search?q=knife+set&refer_code={TEMU_AFFILIATE}",
        "emoji": "🥘"
    },
    {
        "category": "Кухня",
        "title": "🥤 Набор стаканов (6 шт)",
        "description": "Красивые стаканы для напитков. Скидка 60%!",
        "price": "₴79",
        "old_price": "₴199",
        "link": f"https://www.temu.com/ua/search?q=glass+cups&refer_code={TEMU_AFFILIATE}",
        "emoji": "🍷"
    },
]

def get_random_product():
    """Получить случайный товар"""
    return random.choice(PRODUCTS)

def get_products_by_category(category):
    """Получить товары по категории"""
    return [p for p in PRODUCTS if p["category"] == category]

def get_all_categories():
    """Получить все категории"""
    return list(set(p["category"] for p in PRODUCTS))

def format_product_message(product):
    """Форматировать сообщение о товаре"""
    text = f"""<b>{product['emoji']} {product['title']}</b>

{product['description']}

💰 <b>Цена:</b> {product['price']} <s>{product['old_price']}</s>

🔗 <a href="{product['link']}">Заказать на Temu</a>

#temu #скидки #акции #топпредложения #{product['category'].lower()}"""
    return text

if __name__ == "__main__":
    # Тест
    product = get_random_product()
    print(f"Категория: {product['category']}")
    print(f"Товар: {product['title']}")
    print(f"Ссылка: {product['link']}")
    print("\nСообщение:")
    print(format_product_message(product))
