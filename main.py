
import asyncio
from aiogram import Bot,Dispatcher,types
from aiogram.filters import Command
from googletrans import Translator

bot=Bot(token="7683445875:AAHzga6HauU2J69pDjznypS03sfxXj7u8p8")
dp=Dispatcher()

translator = Translator()

@dp.message(Command("start"))
async def cmd_star(message:types.Message):
    await message.answer("Xush kelibsiz! 🌐\n"
                         "Menga matn yuboring, men uni ingliz tiliga tarjima qilaman.\n\n"
                         "Misol: Salom")

@dp.message()
async def translate_message(message: types.Message):
    try:
        user_text=message.text
        detected_lang=translator.detect(user_text).lang

        if detected_lang == "en":
            target_lang = "uz"
        elif detected_lang == "uz":
            target_lang = "en"
        else:
            target_lang = "en"

        translation = translator.translate(user_text, src='auto', dest=target_lang)
        await message.answer(f"📤 Original: {user_text}\n"
                             f"📥 Tarjima: {translation.text}")
    except Exception as e:
        await message.answer("Tarjima qilishda xatolik yuz berdi. Iltimos, qayta urinib ko'ring.")
        print(e)


async def main():
    await dp.start_polling(bot)


if __name__=="__main__":
    asyncio.run(main())