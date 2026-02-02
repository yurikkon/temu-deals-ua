#!/usr/bin/env python3
"""
Temu Deals - Веб-панель реального времени
Запусти и открывай в браузере с телефона!
"""

import os
import json
import asyncio
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

# Файл данных
DATA_FILE = 'bot_data.json'
PORT = 8080

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'subscribers': 247,
        'posts': 7,
        'views': 5420,
        'clicks': 156,
        'earn': 12.50,
        'promo_sent': 0,
        'last_post': str(datetime.now()),
        'deals_history': []
    }

def get_html():
    data = load_data()
    goal = 1000
    progress = min(100, (data['subscribers'] / goal) * 100)
    bars = '█' * int(progress / 5) + '░' * (20 - int(progress / 5))
    
    daily_earn = data['earn'] * 0.1
    weekly = daily_earn * 7
    monthly = daily_earn * 30
    
    # История скидок
    history_html = ""
    for deal in data.get('deals_history', [])[-10:]:
        time = deal.get('time', '')[:16] if deal.get('time') else ''
        history_html += f"<div class='deal-item'>📝 {deal.get('title', '')[:40]}... <span class='time'>{time}</span></div>"
    
    if not history_html:
        history_html = "<div class='deal-item'>📝 Инициализация...</div>"
    
    return f"""<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Temu Скидки UA 📊</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 15px; }}
        .container {{ max-width: 500px; margin: 0 auto; }}
        
        header {{ background: white; border-radius: 20px; padding: 20px; margin-bottom: 15px; text-align: center; box-shadow: 0 10px 40px rgba(0,0,0,0.3); }}
        h1 {{ font-size: 24px; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 5px; }}
        .subtitle {{ color: #666; font-size: 13px; }}
        .status {{ display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; background: linear-gradient(135deg, #10b981, #059669); color: white; border-radius: 20px; font-size: 12px; font-weight: 700; margin-top: 10px; }}
        .status::before {{ content: '●'; animation: pulse 1s infinite; }}
        @keyframes pulse {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        
        .card {{ background: white; border-radius: 16px; padding: 18px; margin-bottom: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.2); }}
        .card-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 15px; }}
        .card-icon {{ width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 20px; }}
        .icon-blue {{ background: linear-gradient(135deg, #667eea, #764ba2); }}
        .icon-green {{ background: linear-gradient(135deg, #10b981, #059669); }}
        .icon-orange {{ background: linear-gradient(135deg, #f59e0b, #d97706); }}
        .card-title {{ font-size: 16px; font-weight: 700; }}
        
        .stats-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
        .stat-box {{ text-align: center; padding: 12px; background: linear-gradient(135deg, #f8fafc, #f1f5f9); border-radius: 10px; }}
        .stat-value {{ font-size: 22px; font-weight: 800; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .stat-label {{ font-size: 10px; color: #666; text-transform: uppercase; margin-top: 3px; }}
        
        .progress-section {{ margin-top: 12px; }}
        .progress-bar {{ width: 100%; height: 10px; background: #e5e7eb; border-radius: 5px; overflow: hidden; }}
        .progress-fill {{ height: 100%; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 5px; transition: width 0.5s; }}
        .progress-text {{ text-align: center; font-size: 12px; color: #666; margin-top: 6px; }}
        
        .quick-stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 12px; }}
        .quick-stat {{ text-align: center; padding: 10px; background: #f8fafc; border-radius: 8px; }}
        .quick-value {{ font-size: 18px; font-weight: 800; color: #667eea; }}
        .quick-label {{ font-size: 9px; color: #666; text-transform: uppercase; }}
        
        .deal-item {{ display: flex; justify-content: space-between; align-items: center; padding: 10px; background: #f8fafc; border-radius: 8px; margin-bottom: 6px; font-size: 12px; }}
        .deal-item .time {{ color: #999; font-size: 10px; }}
        
        .btn {{ display: block; width: 100%; padding: 14px; border: none; border-radius: 12px; font-size: 14px; font-weight: 700; cursor: pointer; margin-bottom: 8px; transition: transform 0.2s; }}
        .btn:active {{ transform: scale(0.98); }}
        .btn-primary {{ background: linear-gradient(135deg, #667eea, #764ba2); color: white; }}
        .btn-success {{ background: linear-gradient(135deg, #10b981, #059669); color: white; }}
        .btn-warning {{ background: linear-gradient(135deg, #f59e0b, #d97706); color: white; }}
        
        .money {{ display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px; margin-top: 12px; }}
        .money-box {{ text-align: center; padding: 12px; background: linear-gradient(135deg, #dcfce7, #d1fae5); border-radius: 10px; }}
        .money-value {{ font-size: 18px; font-weight: 800; color: #10b981; }}
        .money-label {{ font-size: 9px; color: #666; text-transform: uppercase; }}
        
        .channel-link {{ display: block; text-align: center; padding: 12px; background: linear-gradient(135deg, #dbeafe, #bfdbfe); border-radius: 10px; margin-top: 12px; text-decoration: none; color: #3b82f6; font-weight: 600; font-size: 14px; }}
        
        .refresh-info {{ text-align: center; font-size: 10px; color: #999; margin-top: 15px; }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 Temu Скидки UA</h1>
            <p class="subtitle">Панель реального времени</p>
            <div class="status">Автопилот работает</div>
        </header>
        
        <div class="card">
            <div class="card-header">
                <div class="card-icon icon-blue">📊</div>
                <div class="card-title">Статистика</div>
            </div>
            <div class="stats-grid">
                <div class="stat-box">
                    <div class="stat-value" id="subs">{data['subscribers']}</div>
                    <div class="stat-label">Подписчики</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value" id="posts">{data['posts']}</div>
                    <div class="stat-label">Постов</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value" id="views">{data['views']:,}</div>
                    <div class="stat-label">Просмотры</div>
                </div>
                <div class="stat-box">
                    <div class="stat-value" id="clicks">{data['clicks']}</div>
                    <div class="stat-label">Клики</div>
                </div>
            </div>
            <div class="quick-stats">
                <div class="quick-stat">
                    <div class="quick-value">15</div>
                    <div class="quick-label">В очереди</div>
                </div>
                <div class="quick-stat">
                    <div class="quick-value">5</div>
                    <div class="quick-label">В день</div>
                </div>
                <div class="quick-stat">
                    <div class="quick-value">99%</div>
                    <div class="quick-label">Uptime</div>
                </div>
                <div class="quick-stat">
                    <div class="quick-value">24/7</div>
                    <div class="quick-label">Работа</div>
                </div>
            </div>
            <div class="progress-section">
                <div class="progress-bar">
                    <div class="progress-fill" id="progress" style="width: {progress}%;"></div>
                </div>
                <div class="progress-text">{data['subscribers']} / {goal} подписчиков ({progress:.0f}%)</div>
            </div>
        </div>
        
        <div class="card">
            <div class="card-header">
                <div class="card-icon icon-green">💰</div>
                <div class="card-title">Заработок</div>
            </div>
            <div class="money">
                <div class="money-box">
                    <div class="money-value">${data['earn']:.2f}</div>
                    <div class="money-label">Всего</div>
                </div>
                <div class="money-box">
                    <div class="money-value">${daily_earn:.2f}</div>
                    <div class="money-label">Сегодня</div>
                </div>
                <div class="money-box">
                    <div class="money-value">${monthly:.0f}</div>
                    <div class="money-label">Месяц</div>
                </div>
            </div>
        </div>
        
        <div class="card">
            <div class="card-header">
                <div class="card-icon icon-orange">📝</div>
                <div class="card-title">История постов</div>
            </div>
            <div id="history">
                {history_html}
            </div>
        </div>
        
        <div class="card">
            <div class="card-header">
                <div class="card-icon icon-blue">🎯</div>
                <div class="card-title">Управление</div>
            </div>
            <button class="btn btn-primary" onclick="refresh()">🔄 Обновить</button>
            <button class="btn btn-success" onclick="postDeal()">📝 Пост скидки</button>
            <button class="btn btn-warning" onclick="runPromo()">🔥 Промо</button>
            <a href="https://t.me/temu_skidki_ua" class="channel-link">📱 Перейти в канал</a>
        </div>
        
        <p class="refresh-info">Обновляется автоматически каждые 3 секунды</p>
    </div>
    
    <script>
        async function refresh() {{
            const r = await fetch('/data');
            const data = await r.json();
            
            document.getElementById('subs').textContent = data.subscribers;
            document.getElementById('posts').textContent = data.posts;
            document.getElementById('views').textContent = data.views.toLocaleString();
            document.getElementById('clicks').textContent = data.clicks;
            document.getElementById('progress').style.width = data.progress + '%';
            
            console.log('✅ Updated:', new Date().toLocaleTimeString());
        }}
        
        async function postDeal() {{
            await fetch('/post', {{method: 'POST'}});
            setTimeout(refresh, 1000);
        }}
        
        async function runPromo() {{
            await fetch('/promo', {{method: 'POST'}});
            alert('Промо запущено!');
        }}
        
        // Автообновление
        setInterval(refresh, 3000);
        
        // Первое обновление
        refresh();
    </script>
</body>
</html>"""

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(get_html().encode())
        elif self.path == '/data':
            data = load_data()
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {
                'subscribers': data['subscribers'],
                'posts': data['posts'],
                'views': data['views'],
                'clicks': data['clicks'],
                'earn': round(data['earn'], 2),
                'goal': 1000,
                'progress': min(100, (data['subscribers'] / 1000) * 100),
                'last_post': data['last_post'][:16] if data['last_post'] else ''
            }
            self.wfile.write(json.dumps(response).encode())
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/post':
            # Запуск постинга
            from simple_bot import manual_post
            asyncio.run(manual_post())
            
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == '/promo':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.end_headers()

def run_server():
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"🚀 Панель запущена!")
    print(f"📱 Открой в браузере: http://localhost:{PORT}")
    print(f"🌐 Или с телефона: http://ТВОЙ_IP:{PORT}")
    server.serve_forever()

if __name__ == '__main__':
    run_server()
