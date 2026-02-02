# Simple Telegram Deal Poster (No Code Required)
# Just copy-paste this into Google Apps Script

function postToTelegram() {
  // Конфигурация
  const TELEGRAM_TOKEN = 'YOUR_BOT_TOKEN';
  const CHANNEL_ID = '@YOUR_CHANNEL_NAME';
  const AFFILIATE_CODE = 'YOUR_AFFILIATE_CODE';
  
  // Пример сделок (в реальности парсить с Temu)
  const deals = [
    {
      title: '🔥 Беспроводные наушники',
      price: '$19.99',
      oldPrice: '$49.99',
      discount: '60%',
      link: `https://temu.com/ua/headphones?_r=${AFFILIATE_CODE}`
    },
    {
      title: '🔥 Умные часы с пульсометром',
      price: '$29.99',
      oldPrice: '$79.99',
      discount: '62%',
      link: `https://temu.com/ua/smartwatch?_r=${AFFILIATE_CODE}`
    },
    {
      title: '🔥 Набор посуды 12 предметов',
      price: '$24.99',
      oldPrice: '$59.99',
      discount: '58%',
      link: `https://temu.com/ua/cookware?_r=${AFFILIATE_CODE}`
    },
    {
      title: '🔥 Увлажнитель воздуха',
      price: '$14.99',
      oldPrice: '$34.99',
      discount: '57%',
      link: `https://temu.com/ua/humidifier?_r=${AFFILIATE_CODE}`
    },
    {
      title: '🔥 Спортивный костюм Oversize',
      price: '$19.99',
      oldPrice: '$44.99',
      discount: '56%',
      link: `https://temu.com/ua/sportswear?_r=${AFFILIATE_CODE}`
    }
  ];
  
  // Выбираем 3 случайные сделки
  const shuffled = deals.sort(() => 0.5 - Math.random());
  const selectedDeals = shuffled.slice(0, 3);
  
  // Формируем сообщение
  let message = '🔥 <b>ЛУЧШИЕ СКИДКИ ДНЯ</b>\n\n';
  
  selectedDeals.forEach((deal, index) => {
    message += `${index + 1}. ${deal.title}\n`;
    message += `   💰 <s>${deal.oldPrice}</s> → <b>${deal.price}</b>\n`;
    message += `   📉 Скидка: ${deal.discount}\n`;
    message += `   🔗 [Купить](${deal.link})\n\n`;
  });
  
  message += '⏰ Актуально сегодня!';
  
  // Отправляем в Telegram
  const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage`;
  const payload = {
    chat_id: CHANNEL_ID,
    text: message,
    parse_mode: 'HTML',
    disable_web_page_preview: false
  };
  
  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload)
  };
  
  try {
    const response = UrlFetchApp.fetch(url, options);
    Logger.log('Message sent: ' + response.getResponseCode());
  } catch (error) {
    Logger.log('Error: ' + error.toString());
  }
}

// Функция для ручного запуска
function manualPost() {
  postToTelegram();
}
