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
async def delete_games(message: Message):
    game_emojis = {
        "🎰",  # Казино
        "🎯",  # Дартс
        "🎲",  # Кубик
        "🏀",  # Баскетбол
        "⚽",  # Футбол
        "🎳",  # Боулинг
    }

    if message.dice.emoji in game_emojis:
        try:
            await message.delete()
            print(
                f"Удалена игра {message.dice.emoji} от {message.from_user.full_name}"
            )
        except Exception as e:
            print(f"Ошибка удаления: {e}")


async def main():
    print("Бот запущен")

    # Удаляем старый webhook, если он был установлен
    await bot.delete_webhook(drop_pending_updates=True)

    # Запускаем получение сообщений
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
