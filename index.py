from aiogram import Bot, Dispatcher
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F

import asyncio

# Ваш токен бота
API_TOKEN = '7254708854:AAEop3TvQaazXTo8ZWx7djq8jBy1PMo4w-Q'

# URL вашего Telegram Web App (например, ваше веб-приложение)
WEB_APP_URL = 'https://nur521.github.io/ra/'  # Замените на URL вашего Web App

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Хэндлер для команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    # Создаем кнопку для открытия Telegram Web App
    web_app_button = KeyboardButton(text="Open App", web_app=WebAppInfo(url=WEB_APP_URL))
    
    # Создаем клавиатуру с кнопкой Web App
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(web_app_button)
    
    # Отправляем сообщение с кнопкой
    await message.answer("Нажмите на кнопку ниже, чтобы открыть приложение:", reply_markup=keyboard)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
