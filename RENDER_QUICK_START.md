# Инструкция запуска на Render.com (БЕСПЛАТНО 24/7)

## Шаг 1: Регистрация
1. Открой https://render.com
2. Нажми "Get Started" → "GitHub"
3. Авторизуйся через GitHub

## Шаг 2: Создание Web Service
1. Нажми "New +" → "Web Service"
2. Выбери репозиторий с кодом (если не загрузил на GitHub, пропусти)
3. Или выбери "Upload Files" и загрузи архив проекта

## Шаг 3: Настройки
```
Name: temu-deals-bot
Root Directory: .
Build Command: pip install -r requirements.txt
Start Command: python simple_bot.py
```

## Шаг 4: Переменные окружения
Нажми "Advanced" → "Add Environment Variables":

| Key | Value |
|-----|-------|
| TELEGRAM_TOKEN | ТОКЕН_ТВОЕГО_БОТА |
| CHANNEL_ID | @temu_deals_ua |
| TEMU_AFFILIATE_CODE | ТВОЙ_КОД |
| ADMIN_CHAT_ID | ТВОЙ_TELEGRAM_ID |

## Шаг 5: Запуск
1. Нажми "Create Web Service"
2. Подожди 2-3 минуты (установка зависимостей)
3. Проверь логи - должно быть "Система готова!"

## Шаг 6: Проверка
Отправь боту команду /start
Он должен ответить и показать статистику

---

## Альтернатива: Запуск на другом хостинге

### Railway.com
1. Регистрация через GitHub
2. "New Project" → "Deploy from GitHub"
3. Выбери репозиторий
4. Добавь переменные окружения (Environment Variables)
5. Готово!

### Cyclic.sh
1. Регистрация через GitHub
2. "Deploy" → выбери репозиторий
3. Добавь переменные окружения
4. Бесплатно!

### PythonAnywhere.com
1. Регистрация (бесплатный аккаунт)
2. Открой Bash консоль
3. Клонируй репозиторий:
```
git clone https://github.com/ТВОЙ_НИК/temu-deals-ua.git
cd temu-deals-ua
pip install -r requirements.txt
```
4. "Files" → Загрузи requirements.txt и simple_bot.py
5. "Schedule" → Добавь задачу на запуск каждый час

---

## Проблемы и решения

### Бот не отвечает
- Проверь логи на Render.com
- Убедись, что TOKEN правильный
- Проверь, что бот добавлен в канал как администратор

### Ошибка при установке
- Убедись, что Python 3.11
- Проверь requirements.txt

### Канал не найден
- CHANNEL_ID должен быть с @ в начале
- Бот должен быть администратором канала

---

## Команды бота
- /start - запуск и статистика
- /stats - показать статистику
- /post - опубликовать скидку вручную
- /help - помощь

## Настройка автопостинга
Автопостинг уже настроен на 5 раз в день:
- 09:00, 12:00, 15:00, 18:00, 21:00

Изменить время можно в simple_bot.py:
```python
if hour in [9, 12, 15, 18, 21]:
```
