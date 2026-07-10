import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = "8796297557:AAHo_gnivB9Me2i6d58mabtZFEaSWqM7ltg"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(F.dice)
async def delete_games(message: Message):
    game_emojis = {
        "🎰",
        "🎯",
        "🎲",
        "🏀",
        "⚽",
        "🎳",
    }

    if message.dice.emoji in game_emojis:
        try:
            await message.delete()
            print(f"Удалена игра {message.dice.emoji}")
        except Exception as e:
            print(e)


async def main():
    print("Бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
