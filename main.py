import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# --- Data Definition (Step 2) ---
PORTFOLIO_DATA = {
    "github_url": "github.com/nataku-45",
    "services": [
        {"title": "Разработка MVP", "description": "Быстрая реализация прототипа вашего проекта для проверки идеи."},
        {"title": "Автоматизация", "description": "Написание скриптов для решения рутинных или несложных технических задач."},
        {"title": "Поддержка", "description": "Работа с чужим кодом, внесение правок и доработок."},
    ],
    "tech_stack": {
        "backend": ["Flask", "Django", "FastAPI"],
        "data_automation": ["BeautifulSoup4", "Requests", "Selenium", "Pandas"],
        "telegram_bots": ["Aiogram", "PyTelegramBotAPI"]
    },
    "work_conditions": "Стоимость и сроки выполнения рассчитываются индивидуально. Всё зависит от сложности технического задания и объема работ. Я открыт к обсуждению, чтобы найти комфортное решение для обеих сторон."
}

# --- FastAPI Setup and Templating (Step 3) ---
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# --- Main Page Route (Step 5) ---
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": PORTFOLIO_DATA})

# --- Async Demo Endpoint (Step 6) ---
@app.get("/demo/async_task")
async def demo_async_task():
    # Simulate an I/O bound async task (e.g., external API call or heavy processing)
    await asyncio.sleep(1.5) 
    return {"message": "Асинхронная задача на 1.5 секунды выполнена успешно!", "tech_used": "FastAPI/Async"}