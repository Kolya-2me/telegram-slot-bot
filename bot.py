import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Не найдена переменная окружения BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.dice)
async def delete_slot(message: Message):
    if message.dice.emoji == "🎰":
        try:
            await message.delete()
            print(f"Удалено сообщение с 🎰 от {message.from_user.full_name}")
        except Exception as e:
            print(f"Ошибка удаления: {e}")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
