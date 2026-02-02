# Инструкция загрузки на GitHub (1 минута)

## Шаг 1: Создай репозиторий на github.com
1. Открой https://github.com/new
2. Введи имя: **temu-deals-ua**
3. Выбери **Public**
4. НЕ ставь галочку "Add a README file"
5. Нажми **Create repository**

## Шаг 2: Загрузи файлы
Сейчас я создам ZIP файл для загрузки...

## Шаг 3: Настрой GitHub Actions (автозапуск)
После загрузки:
1. Зайди в репозиторий → Settings → Secrets
2. Добавь секреты:
   - `TELEGRAM_TOKEN` - твой токен бота
   - `TELEGRAM_CHANNEL` - @temu_deals_ua
   - `TG_API_ID` - твой API ID
   - `TG_API_HASH` - твой API Hash

Автопостинг запустится автоматически!

