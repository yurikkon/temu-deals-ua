"""
Cross-posting to Reddit, Twitter, and Facebook
Кросс-постинг на Reddit, Twitter и Facebook
"""

import os
import praw
import tweepy
import requests
from temu_products import get_random_product, format_product_message

# ============ REDDIT ============
def post_to_reddit(product):
    """Постить на Reddit"""
    try:
        reddit = praw.Reddit(
            client_id=os.environ.get('REDDIT_CLIENT_ID'),
            client_secret=os.environ.get('REDDIT_CLIENT_SECRET'),
            user_agent=os.environ.get('REDDIT_USER_AGENT', 'TemuDealsBot/1.0'),
            username=os.environ.get('REDDIT_USERNAME'),
            password=os.environ.get('REDDIT_PASSWORD')
        )
        
        # Выбираем сабреддиты для постинга
        subreddits = ['deals', 'discounts', 'ukraine', 'shopping']
        
        for subreddit_name in subreddits:
            try:
                subreddit = reddit.subreddit(subreddit_name)
                
                title = f"{product['emoji']} {product['title']} - {product['price']} (было {product['old_price']})"
                
                # Форматируем текст для Reddit
                text = f"""{product['description']}

**Цена:** {product['price']} ~~{product['old_price']}~~

**Ссылка:** {product['link']}

**Категория:** {product['category']}

---
*Это автоматический пост с лучшими скидками на Temu*
"""
                
                subreddit.submit(title=title, selftext=text)
                print(f"✅ Posted to r/{subreddit_name}: {product['title']}")
            except Exception as e:
                print(f"❌ Error posting to r/{subreddit_name}: {e}")
                
    except Exception as e:
        print(f"❌ Reddit error: {e}")

# ============ TWITTER ============
def post_to_twitter(product):
    """Постить на Twitter"""
    try:
        client = tweepy.Client(
            bearer_token=os.environ.get('TWITTER_BEARER_TOKEN'),
            consumer_key=os.environ.get('TWITTER_API_KEY'),
            consumer_secret=os.environ.get('TWITTER_API_SECRET'),
            access_token=os.environ.get('TWITTER_ACCESS_TOKEN'),
            access_token_secret=os.environ.get('TWITTER_ACCESS_SECRET')
        )
        
        # Форматируем текст для Twitter (макс 280 символов)
        text = f"""{product['emoji']} {product['title']}

{product['price']} (было {product['old_price']})

🔗 {product['link']}

#Temu #TemuDeals #Скидки #Shopping"""
        
        # Если текст слишком длинный, сокращаем
        if len(text) > 280:
            text = f"{product['emoji']} {product['title']}\n{product['price']} (было {product['old_price']})\n🔗 {product['link']}\n#Temu #Скидки"
        
        response = client.create_tweet(text=text)
        print(f"✅ Posted to Twitter: {product['title']}")
        
    except Exception as e:
        print(f"❌ Twitter error: {e}")

# ============ FACEBOOK ============
def post_to_facebook(product):
    """Постить на Facebook"""
    try:
        page_id = os.environ.get('FACEBOOK_PAGE_ID')
        access_token = os.environ.get('FACEBOOK_ACCESS_TOKEN')
        
        if not page_id or not access_token:
            print("❌ Facebook credentials not set")
            return
        
        url = f"https://graph.facebook.com/{page_id}/feed"
        
        # Форматируем текст для Facebook
        message = f"""{product['emoji']} {product['title']}

{product['description']}

💰 Цена: {product['price']} (было {product['old_price']})

🔗 Заказать: {product['link']}

#Temu #Скидки #Акции #Покупки"""
        
        payload = {
            'message': message,
            'access_token': access_token
        }
        
        response = requests.post(url, data=payload)
        
        if response.status_code == 200:
            print(f"✅ Posted to Facebook: {product['title']}")
        else:
            print(f"❌ Facebook error: {response.text}")
            
    except Exception as e:
        print(f"❌ Facebook error: {e}")

# ============ MAIN ============
def cross_post_product(product=None):
    """Постить товар на все платформы"""
    if product is None:
        product = get_random_product()
    
    print(f"\n📢 Cross-posting: {product['title']}")
    print(f"   Category: {product['category']}")
    print(f"   Price: {product['price']}")
    
    # Постим на все платформы
    if os.environ.get('REDDIT_CLIENT_ID'):
        post_to_reddit(product)
    else:
        print("⚠️  Reddit credentials not set")
    
    if os.environ.get('TWITTER_BEARER_TOKEN'):
        post_to_twitter(product)
    else:
        print("⚠️  Twitter credentials not set")
    
    if os.environ.get('FACEBOOK_PAGE_ID'):
        post_to_facebook(product)
    else:
        print("⚠️  Facebook credentials not set")

if __name__ == "__main__":
    product = get_random_product()
    cross_post_product(product)
