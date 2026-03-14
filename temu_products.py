"""
Temu Products Database - 100+ Unique Products
Большая база товаров с 100+ уникальными товарами
"""

import os
import random
from datetime import datetime

TEMU_AFFILIATE = os.environ.get('TEMU_AFFILIATE_CODE', 'ale040196')

# 100+ УНИКАЛЬНЫХ ТОВАРОВ - БЕЗ ПОВТОРЕНИЙ!
PRODUCTS = [
    # ===== ЭЛЕКТРОНИКА (20 товаров) =====
    {"category": "Электроника", "title": "🎧 Беспроводные наушники TWS", "description": "Качественные наушники с шумоподавлением. Батарея 30+ часов.", "price": "₴299", "old_price": "₴749", "link": f"https://www.temu.com/ua/search?q=wireless+earbuds&refer_code={TEMU_AFFILIATE}", "emoji": "🎧"},
    {"category": "Электроника", "title": "📱 Защитное стекло для телефона", "description": "Закаленное стекло 9H для всех моделей.", "price": "₴49", "old_price": "₴159", "link": f"https://www.temu.com/ua/search?q=tempered+glass&refer_code={TEMU_AFFILIATE}", "emoji": "🛡️"},
    {"category": "Электроника", "title": "🔋 Power Bank 20000mAh", "description": "Портативное зарядное с быстрой зарядкой.", "price": "₴199", "old_price": "₴399", "link": f"https://www.temu.com/ua/search?q=power+bank&refer_code={TEMU_AFFILIATE}", "emoji": "⚡"},
    {"category": "Электроника", "title": "🖱️ Беспроводная мышка", "description": "Удобная мышка с батареей на 18 месяцев.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=wireless+mouse&refer_code={TEMU_AFFILIATE}", "emoji": "🖱️"},
    {"category": "Электроника", "title": "⌨️ Механическая клавиатура", "description": "RGB подсветка, 104 клавиши, USB.", "price": "₴349", "old_price": "₴899", "link": f"https://www.temu.com/ua/search?q=mechanical+keyboard&refer_code={TEMU_AFFILIATE}", "emoji": "⌨️"},
    {"category": "Электроника", "title": "📷 Мини камера 4K", "description": "Портативная камера с ночным видением.", "price": "₴599", "old_price": "₴1499", "link": f"https://www.temu.com/ua/search?q=mini+camera+4k&refer_code={TEMU_AFFILIATE}", "emoji": "📷"},
    {"category": "Электроника", "title": "🔌 USB-C кабель (3 шт)", "description": "Прочные кабели длиной 2м каждый.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=usb+c+cable&refer_code={TEMU_AFFILIATE}", "emoji": "🔌"},
    {"category": "Электроника", "title": "💡 LED лампочки (4 шт)", "description": "Энергосберегающие лампы E27.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=led+bulbs&refer_code={TEMU_AFFILIATE}", "emoji": "💡"},
    {"category": "Электроника", "title": "🎙️ Микрофон конденсаторный", "description": "Профессиональный микрофон для стриминга.", "price": "₴449", "old_price": "₴1199", "link": f"https://www.temu.com/ua/search?q=condenser+microphone&refer_code={TEMU_AFFILIATE}", "emoji": "🎙️"},
    {"category": "Электроника", "title": "📡 WiFi роутер 6", "description": "Скорость до 1200 Mbps, 4 антенны.", "price": "₴299", "old_price": "₴799", "link": f"https://www.temu.com/ua/search?q=wifi+router&refer_code={TEMU_AFFILIATE}", "emoji": "📡"},
    {"category": "Электроника", "title": "🔦 Фонарик LED 10000 люмен", "description": "Мощный фонарик с батареей.", "price": "₴149", "old_price": "₴399", "link": f"https://www.temu.com/ua/search?q=led+flashlight&refer_code={TEMU_AFFILIATE}", "emoji": "🔦"},
    {"category": "Электроника", "title": "⏱️ Смарт часы", "description": "Фитнес трекер, пульсометр, уведомления.", "price": "₴199", "old_price": "₴599", "link": f"https://www.temu.com/ua/search?q=smart+watch&refer_code={TEMU_AFFILIATE}", "emoji": "⏱️"},
    {"category": "Электроника", "title": "🎮 Геймпад беспроводной", "description": "Совместим с ПК и консолями.", "price": "₴249", "old_price": "₴649", "link": f"https://www.temu.com/ua/search?q=wireless+gamepad&refer_code={TEMU_AFFILIATE}", "emoji": "🎮"},
    {"category": "Электроника", "title": "📞 Держатель для телефона", "description": "Универсальный держатель на присосках.", "price": "₴39", "old_price": "₴99", "link": f"https://www.temu.com/ua/search?q=phone+holder&refer_code={TEMU_AFFILIATE}", "emoji": "📞"},
    {"category": "Электроника", "title": "🔊 Портативная колонка", "description": "Bluetooth колонка с басом, 12 часов.", "price": "₴179", "old_price": "₴499", "link": f"https://www.temu.com/ua/search?q=bluetooth+speaker&refer_code={TEMU_AFFILIATE}", "emoji": "🔊"},
    {"category": "Электроника", "title": "🎬 Кабель HDMI 2м", "description": "4K поддержка, позолоченные контакты.", "price": "₴59", "old_price": "₴149", "link": f"https://www.temu.com/ua/search?q=hdmi+cable&refer_code={TEMU_AFFILIATE}", "emoji": "🎬"},
    {"category": "Электроника", "title": "🖥️ Подставка для ноутбука", "description": "Алюминиевая подставка, регулируемая.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=laptop+stand&refer_code={TEMU_AFFILIATE}", "emoji": "🖥️"},
    {"category": "Электроника", "title": "🌡️ Цифровой термометр", "description": "Бесконтактный инфракрасный.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=digital+thermometer&refer_code={TEMU_AFFILIATE}", "emoji": "🌡️"},
    {"category": "Электроника", "title": "🔐 Умный замок", "description": "Отпирание по отпечатку пальца.", "price": "₴599", "old_price": "₴1499", "link": f"https://www.temu.com/ua/search?q=smart+lock&refer_code={TEMU_AFFILIATE}", "emoji": "🔐"},
    {"category": "Электроника", "title": "⚙️ Набор отвёрток 120 шт", "description": "Профессиональный набор инструментов.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=screwdriver+set&refer_code={TEMU_AFFILIATE}", "emoji": "⚙️"},

    # ===== ОДЕЖДА (20 товаров) =====
    {"category": "Одежда", "title": "👕 Летние футболки (3 шт)", "description": "Хлопковые футболки разных цветов.", "price": "₴149", "old_price": "₴429", "link": f"https://www.temu.com/ua/search?q=t-shirt+men&refer_code={TEMU_AFFILIATE}", "emoji": "👔"},
    {"category": "Одежда", "title": "👟 Спортивные кроссовки", "description": "Удобные кроссовки для спорта.", "price": "₴249", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=sports+shoes&refer_code={TEMU_AFFILIATE}", "emoji": "🏃"},
    {"category": "Одежда", "title": "🧢 Кепка бейсболка", "description": "Стильная кепка для защиты от солнца.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=baseball+cap&refer_code={TEMU_AFFILIATE}", "emoji": "🎩"},
    {"category": "Одежда", "title": "🧥 Куртка ветровка", "description": "Легкая куртка на весну-осень.", "price": "₴349", "old_price": "₴899", "link": f"https://www.temu.com/ua/search?q=windbreaker+jacket&refer_code={TEMU_AFFILIATE}", "emoji": "🧥"},
    {"category": "Одежда", "title": "👖 Джинсы классические", "description": "Удобные джинсы синего цвета.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=classic+jeans&refer_code={TEMU_AFFILIATE}", "emoji": "👖"},
    {"category": "Одежда", "title": "🧣 Шарф теплый", "description": "Мягкий шарф из акрила.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=warm+scarf&refer_code={TEMU_AFFILIATE}", "emoji": "🧣"},
    {"category": "Одежда", "title": "🧤 Перчатки зимние", "description": "Теплые перчатки с сенсором.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=winter+gloves&refer_code={TEMU_AFFILIATE}", "emoji": "🧤"},
    {"category": "Одежда", "title": "🩳 Шорты спортивные", "description": "Удобные шорты для спорта.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=sports+shorts&refer_code={TEMU_AFFILIATE}", "emoji": "🩳"},
    {"category": "Одежда", "title": "👔 Рубашка деловая", "description": "Классическая рубашка белого цвета.", "price": "₴179", "old_price": "₴499", "link": f"https://www.temu.com/ua/search?q=business+shirt&refer_code={TEMU_AFFILIATE}", "emoji": "👔"},
    {"category": "Одежда", "title": "🧦 Носки (12 пар)", "description": "Комфортные носки разных цветов.", "price": "₴59", "old_price": "₴149", "link": f"https://www.temu.com/ua/search?q=socks+pack&refer_code={TEMU_AFFILIATE}", "emoji": "🧦"},
    {"category": "Одежда", "title": "👗 Платье летнее", "description": "Легкое платье для жаркой погоды.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=summer+dress&refer_code={TEMU_AFFILIATE}", "emoji": "👗"},
    {"category": "Одежда", "title": "🎽 Спортивный топ", "description": "Топ для йоги и фитнеса.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=sports+top&refer_code={TEMU_AFFILIATE}", "emoji": "🎽"},
    {"category": "Одежда", "title": "👞 Туфли классические", "description": "Черные туфли для офиса.", "price": "₴249", "old_price": "₴649", "link": f"https://www.temu.com/ua/search?q=classic+shoes&refer_code={TEMU_AFFILIATE}", "emoji": "👞"},
    {"category": "Одежда", "title": "🧢 Панама летняя", "description": "Широкополая панама для пляжа.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=summer+hat&refer_code={TEMU_AFFILIATE}", "emoji": "🎩"},
    {"category": "Одежда", "title": "🧥 Пуховик зимний", "description": "Теплый пуховик на зиму.", "price": "₴599", "old_price": "₴1499", "link": f"https://www.temu.com/ua/search?q=winter+parka&refer_code={TEMU_AFFILIATE}", "emoji": "🧥"},
    {"category": "Одежда", "title": "👜 Рюкзак городской", "description": "Удобный рюкзак 30л.", "price": "₴179", "old_price": "₴499", "link": f"https://www.temu.com/ua/search?q=urban+backpack&refer_code={TEMU_AFFILIATE}", "emoji": "👜"},
    {"category": "Одежда", "title": "👛 Сумка через плечо", "description": "Практичная сумка для города.", "price": "₴149", "old_price": "₴399", "link": f"https://www.temu.com/ua/search?q=shoulder+bag&refer_code={TEMU_AFFILIATE}", "emoji": "👛"},
    {"category": "Одежда", "title": "⌚ Ремень кожаный", "description": "Классический кожаный ремень.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=leather+belt&refer_code={TEMU_AFFILIATE}", "emoji": "⌚"},
    {"category": "Одежда", "title": "🕶️ Солнцезащитные очки", "description": "Стильные очки UV400.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=sunglasses&refer_code={TEMU_AFFILIATE}", "emoji": "🕶️"},
    {"category": "Одежда", "title": "💍 Часы наручные", "description": "Классические часы с кожаным ремешком.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=wrist+watch&refer_code={TEMU_AFFILIATE}", "emoji": "⌚"},

    # ===== ДОМ (20 товаров) =====
    {"category": "Дом", "title": "🛏️ Комплект постельного белья", "description": "Мягкое белье 4 предмета.", "price": "₴299", "old_price": "₴599", "link": f"https://www.temu.com/ua/search?q=bedding+set&refer_code={TEMU_AFFILIATE}", "emoji": "🛌"},
    {"category": "Дом", "title": "🎀 Декоративные подушки (2 шт)", "description": "Красивые подушки для дивана.", "price": "₴129", "old_price": "₴289", "link": f"https://www.temu.com/ua/search?q=decorative+pillows&refer_code={TEMU_AFFILIATE}", "emoji": "🎀"},
    {"category": "Дом", "title": "💡 LED лампочки (4 шт)", "description": "Энергосберегающие лампы.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=led+bulbs&refer_code={TEMU_AFFILIATE}", "emoji": "💡"},
    {"category": "Дом", "title": "🧹 Набор для уборки", "description": "Щетка, совок, тряпки.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=cleaning+set&refer_code={TEMU_AFFILIATE}", "emoji": "🧹"},
    {"category": "Дом", "title": "🪴 Горшок для цветов", "description": "Керамический горшок 20см.", "price": "₴49", "old_price": "₴129", "link": f"https://www.temu.com/ua/search?q=flower+pot&refer_code={TEMU_AFFILIATE}", "emoji": "🪴"},
    {"category": "Дом", "title": "🕯️ Ароматические свечи (3 шт)", "description": "Свечи с приятным ароматом.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=scented+candles&refer_code={TEMU_AFFILIATE}", "emoji": "🕯️"},
    {"category": "Дом", "title": "🧴 Органайзер для ванной", "description": "Пластиковый органайзер.", "price": "₴59", "old_price": "₴149", "link": f"https://www.temu.com/ua/search?q=bathroom+organizer&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Дом", "title": "🪞 Зеркало настенное", "description": "Круглое зеркало 40см.", "price": "₴149", "old_price": "₴399", "link": f"https://www.temu.com/ua/search?q=wall+mirror&refer_code={TEMU_AFFILIATE}", "emoji": "🪞"},
    {"category": "Дом", "title": "🛁 Коврик для ванной", "description": "Противоскользящий коврик.", "price": "₴69", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=bath+mat&refer_code={TEMU_AFFILIATE}", "emoji": "🛁"},
    {"category": "Дом", "title": "🧺 Корзина для белья", "description": "Тканевая корзина 40л.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=laundry+basket&refer_code={TEMU_AFFILIATE}", "emoji": "🧺"},
    {"category": "Дом", "title": "🪟 Шторы блэкаут", "description": "Темные шторы 2м х 2.5м.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=blackout+curtains&refer_code={TEMU_AFFILIATE}", "emoji": "🪟"},
    {"category": "Дом", "title": "🛋️ Чехол для дивана", "description": "Универсальный чехол.", "price": "₴179", "old_price": "₴499", "link": f"https://www.temu.com/ua/search?q=sofa+cover&refer_code={TEMU_AFFILIATE}", "emoji": "🛋️"},
    {"category": "Дом", "title": "🧽 Губки для посуды (10 шт)", "description": "Мягкие губки для мытья.", "price": "₴39", "old_price": "₴99", "link": f"https://www.temu.com/ua/search?q=dish+sponges&refer_code={TEMU_AFFILIATE}", "emoji": "🧽"},
    {"category": "Дом", "title": "🧴 Контейнеры для хранения (3 шт)", "description": "Пластиковые контейнеры.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=storage+containers&refer_code={TEMU_AFFILIATE}", "emoji": "📦"},
    {"category": "Дом", "title": "🕯️ Люстра потолочная", "description": "Современная люстра LED.", "price": "₴349", "old_price": "₴899", "link": f"https://www.temu.com/ua/search?q=ceiling+lamp&refer_code={TEMU_AFFILIATE}", "emoji": "💡"},
    {"category": "Дом", "title": "🧹 Швабра с ведром", "description": "Швабра с отжимом.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=mop+bucket&refer_code={TEMU_AFFILIATE}", "emoji": "🧹"},
    {"category": "Дом", "title": "🪴 Подставка для цветов", "description": "Деревянная подставка.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=plant+stand&refer_code={TEMU_AFFILIATE}", "emoji": "🪴"},
    {"category": "Дом", "title": "🧴 Диспенсер для мыла", "description": "Автоматический диспенсер.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=soap+dispenser&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Дом", "title": "🧹 Щетка для чистки", "description": "Жесткая щетка для уборки.", "price": "₴49", "old_price": "₴129", "link": f"https://www.temu.com/ua/search?q=cleaning+brush&refer_code={TEMU_AFFILIATE}", "emoji": "🧹"},
    {"category": "Дом", "title": "🪞 Полка настенная", "description": "Деревянная полка 60см.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=wall+shelf&refer_code={TEMU_AFFILIATE}", "emoji": "🪞"},

    # ===== КРАСОТА (20 товаров) =====
    {"category": "Красота", "title": "💄 Набор косметики (12 шт)", "description": "Полный набор для макияжа.", "price": "₴179", "old_price": "₴509", "link": f"https://www.temu.com/ua/search?q=makeup+set&refer_code={TEMU_AFFILIATE}", "emoji": "💅"},
    {"category": "Красота", "title": "🧴 Маска для лица (10 шт)", "description": "Тканевые маски разных типов.", "price": "₴89", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=face+mask&refer_code={TEMU_AFFILIATE}", "emoji": "🧖"},
    {"category": "Красота", "title": "🧴 Набор средств для ухода", "description": "Шампунь, кондиционер, маска.", "price": "₴149", "old_price": "₴329", "link": f"https://www.temu.com/ua/search?q=hair+care&refer_code={TEMU_AFFILIATE}", "emoji": "💆"},
    {"category": "Красота", "title": "💅 Лак для ногтей (12 цветов)", "description": "Набор лаков разных оттенков.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=nail+polish&refer_code={TEMU_AFFILIATE}", "emoji": "💅"},
    {"category": "Красота", "title": "🧴 Крем для лица", "description": "Увлажняющий крем 50мл.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=face+cream&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "🧴 Гель для душа (3 шт)", "description": "Ароматный гель для тела.", "price": "₴69", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=body+wash&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "🧴 Шампунь для волос", "description": "Профессиональный шампунь 500мл.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=shampoo&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "💄 Помада для губ (6 шт)", "description": "Набор помад разных цветов.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=lipstick+set&refer_code={TEMU_AFFILIATE}", "emoji": "💄"},
    {"category": "Красота", "title": "🧴 Тоник для лица", "description": "Очищающий тоник 200мл.", "price": "₴69", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=face+toner&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "💅 Пилка для ногтей (5 шт)", "description": "Набор пилок разной зернистости.", "price": "₴39", "old_price": "₴99", "link": f"https://www.temu.com/ua/search?q=nail+file&refer_code={TEMU_AFFILIATE}", "emoji": "💅"},
    {"category": "Красота", "title": "🧴 Сыворотка для лица", "description": "Антивозрастная сыворотка 30мл.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=face+serum&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "🧴 Маска для волос", "description": "Восстанавливающая маска 200мл.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=hair+mask&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "💄 Тени для век (12 цветов)", "description": "Палетка теней разных оттенков.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=eyeshadow+palette&refer_code={TEMU_AFFILIATE}", "emoji": "💄"},
    {"category": "Красота", "title": "🧴 Дезодорант (3 шт)", "description": "Антиперспирант 48 часов.", "price": "₴59", "old_price": "₴149", "link": f"https://www.temu.com/ua/search?q=deodorant&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "💅 Щипцы для завивки", "description": "Электрические щипцы для волос.", "price": "₴149", "old_price": "₴399", "link": f"https://www.temu.com/ua/search?q=hair+curler&refer_code={TEMU_AFFILIATE}", "emoji": "💅"},
    {"category": "Красота", "title": "🧴 Солнцезащитный крем", "description": "SPF 50+ защита 100мл.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=sunscreen&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "💄 Кисти для макияжа (12 шт)", "description": "Профессиональный набор кистей.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=makeup+brushes&refer_code={TEMU_AFFILIATE}", "emoji": "💄"},
    {"category": "Красота", "title": "🧴 Лосьон для тела", "description": "Увлажняющий лосьон 250мл.", "price": "₴69", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=body+lotion&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},
    {"category": "Красота", "title": "💅 Фен для волос", "description": "Мощный фен 2000W.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=hair+dryer&refer_code={TEMU_AFFILIATE}", "emoji": "💅"},
    {"category": "Красота", "title": "🧴 Пенка для умывания", "description": "Мягкая пенка 150мл.", "price": "₴59", "old_price": "₴149", "link": f"https://www.temu.com/ua/search?q=face+wash&refer_code={TEMU_AFFILIATE}", "emoji": "🧴"},

    # ===== СПОРТ (20 товаров) =====
    {"category": "Спорт", "title": "💪 Гантели (2 шт)", "description": "Регулируемые гантели 2-10 кг.", "price": "₴249", "old_price": "₴499", "link": f"https://www.temu.com/ua/search?q=dumbbells&refer_code={TEMU_AFFILIATE}", "emoji": "💪"},
    {"category": "Спорт", "title": "🧘 Коврик для йоги", "description": "Нескользящий коврик 6мм.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=yoga+mat&refer_code={TEMU_AFFILIATE}", "emoji": "🧘"},
    {"category": "Спорт", "title": "⌚ Фитнес браслет", "description": "Умный браслет с пульсометром.", "price": "₴199", "old_price": "₴439", "link": f"https://www.temu.com/ua/search?q=fitness+tracker&refer_code={TEMU_AFFILIATE}", "emoji": "📊"},
    {"category": "Спорт", "title": "🏋️ Скакалка", "description": "Скоростная скакалка с счетчиком.", "price": "₴49", "old_price": "₴129", "link": f"https://www.temu.com/ua/search?q=jump+rope&refer_code={TEMU_AFFILIATE}", "emoji": "🏋️"},
    {"category": "Спорт", "title": "🤸 Резинки для фитнеса (5 шт)", "description": "Набор резинок разной жесткости.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=resistance+bands&refer_code={TEMU_AFFILIATE}", "emoji": "🤸"},
    {"category": "Спорт", "title": "🏃 Кроссовки для бега", "description": "Профессиональные кроссовки.", "price": "₴349", "old_price": "₴899", "link": f"https://www.temu.com/ua/search?q=running+shoes&refer_code={TEMU_AFFILIATE}", "emoji": "🏃"},
    {"category": "Спорт", "title": "🧘 Блок для йоги", "description": "Пенный блок для йоги.", "price": "₴39", "old_price": "₴99", "link": f"https://www.temu.com/ua/search?q=yoga+block&refer_code={TEMU_AFFILIATE}", "emoji": "🧘"},
    {"category": "Спорт", "title": "⚽ Мяч для фитнеса", "description": "Фитбол 65см.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=exercise+ball&refer_code={TEMU_AFFILIATE}", "emoji": "⚽"},
    {"category": "Спорт", "title": "🏋️ Штанга разборная", "description": "Штанга 20кг с блинами.", "price": "₴599", "old_price": "₴1499", "link": f"https://www.temu.com/ua/search?q=barbell+set&refer_code={TEMU_AFFILIATE}", "emoji": "🏋️"},
    {"category": "Спорт", "title": "🧘 Ремень для йоги", "description": "Хлопковый ремень 2.5м.", "price": "₴39", "old_price": "₴99", "link": f"https://www.temu.com/ua/search?q=yoga+strap&refer_code={TEMU_AFFILIATE}", "emoji": "🧘"},
    {"category": "Спорт", "title": "🏃 Спортивная сумка", "description": "Вместительная спортивная сумка.", "price": "₴149", "old_price": "₴399", "link": f"https://www.temu.com/ua/search?q=sports+bag&refer_code={TEMU_AFFILIATE}", "emoji": "👜"},
    {"category": "Спорт", "title": "🧘 Подушка для медитации", "description": "Круглая подушка для йоги.", "price": "₴69", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=meditation+cushion&refer_code={TEMU_AFFILIATE}", "emoji": "🧘"},
    {"category": "Спорт", "title": "🏋️ Гиря", "description": "Чугунная гиря 16кг.", "price": "₴199", "old_price": "₴549", "link": f"https://www.temu.com/ua/search?q=kettlebell&refer_code={TEMU_AFFILIATE}", "emoji": "🏋️"},
    {"category": "Спорт", "title": "🤸 Коврик для отжиманий", "description": "Толстый коврик 10мм.", "price": "₴89", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=push+up+mat&refer_code={TEMU_AFFILIATE}", "emoji": "🤸"},
    {"category": "Спорт", "title": "⌚ Спортивные часы", "description": "Часы с GPS и пульсометром.", "price": "₴349", "old_price": "₴899", "link": f"https://www.temu.com/ua/search?q=sports+watch&refer_code={TEMU_AFFILIATE}", "emoji": "⌚"},
    {"category": "Спорт", "title": "🏃 Компрессионные носки", "description": "Носки для спорта и восстановления.", "price": "₴99", "old_price": "₴249", "link": f"https://www.temu.com/ua/search?q=compression+socks&refer_code={TEMU_AFFILIATE}", "emoji": "🧦"},
    {"category": "Спорт", "title": "🧘 Валик для массажа", "description": "Массажный валик 30см.", "price": "₴79", "old_price": "₴199", "link": f"https://www.temu.com/ua/search?q=massage+roller&refer_code={TEMU_AFFILIATE}", "emoji": "🧘"},
    {"category": "Спорт", "title": "🏋️ Перчатки для тренировки", "description": "Спортивные перчатки.", "price": "₴69", "old_price": "₴179", "link": f"https://www.temu.com/ua/search?q=workout+gloves&refer_code={TEMU_AFFILIATE}", "emoji": "🧤"},
    {"category": "Спорт", "title": "🤸 Степ платформа", "description": "Регулируемая степ платформа.", "price": "₴129", "old_price": "₴349", "link": f"https://www.temu.com/ua/search?q=step+platform&refer_code={TEMU_AFFILIATE}", "emoji": "🤸"},
    {"category": "Спорт", "title": "⚽ Скейтборд", "description": "Профессиональный скейтборд.", "price": "₴249", "old_price": "₴649", "link": f"https://www.temu.com/ua/search?q=skateboard&refer_code={TEMU_AFFILIATE}", "emoji": "🛹"},
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
    print(f"📊 Всего товаров: {len(PRODUCTS)}")
    print(f"📂 Категорий: {len(get_all_categories())}")
    print(f"\nКатегории:")
    for cat in get_all_categories():
        count = len(get_products_by_category(cat))
        print(f"  - {cat}: {count} товаров")
    
    print(f"\n🎲 Случайные товары:")
    for i in range(5):
        product = get_random_product()
        print(f"  {i+1}. {product['title']} ({product['category']})")
