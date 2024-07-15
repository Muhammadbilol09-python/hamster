from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, CallbackQuery, ParseMode
from inline import royhatim, repleymar
import logging

# Bot tokenini o'zgartiring
API_TOKEN = '7156801086:AAGGWw0g-pvrNwqlKivM7765BDJ9aN_20wA'

# Botni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


msg = f"[Qo'llamaning to'liq versiyasi.](https://hamster-kombat.notion.site/Hamster-Kombat-manual-7e53c342eef143de8bc9c8262ea3a36d)\n\n💰Tangalar uchun bosing\nEkranga teging va tangalarni to'plang\n\\n⛏Qazish\nPassiv daromad olish imkoniyatini beradigan kartalarni yangilang.\n\n⏰Soatlik foyda\nO'yinda 3 soat bo'lmaganingizda ham kartalar siz uchun mustaqil ishlaydi. Keyin yana o'yinga kirishingiz kerak bo'lad\n\n📈LVL\nSizning balansingizda qancha tangalar bo'lsa - almashinuv darajasi shunchalik yuqori bo'ladi. Daraja qanchalik baland bo'lsa, shunchalik tez ko'proq tanga olishingiz mumkin.\n\n\n👥Do'stlar\nDo'stlaringizni taklif qiling va bonuslarga ega bo'ling. Do'stingizga keyingi ligaga chiqishi uchun yordam bering va siz yanada ko'proq bonuslarga ega bo'lasiz.\n\n\n🪙 Token listing\nMavsum oxirida token chiqariladi va o'yinchilar o'rtasida taqsimlanadi. Sanalar kanalimizda e'lon qilinadi. Yangiliklarni kuzatib va xabardor bo'ling. Biz bilan qoling!"


# /start buyrug'i uchun funksiya
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("[salom](https://hamster-kombat.notion.site/Hamster-Kombat-manual-7e53c342eef143de8bc9c8262ea3a36d)",reply_markup=repleymar)


@dp.callback_query_handler(text="odiysoz90")
async def show_contact_keys(call: CallbackQuery):
    callback_data = call.data
    await call.message.reply(msg, parse_mode=ParseMode.MARKDOWN, reply_markup=royhatim)
    await call.answer(cache_time=60)


if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)
