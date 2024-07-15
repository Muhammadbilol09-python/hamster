from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

repleymar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1 bosishda o'ynang 🐹", web_app=WebAppInfo(url="https://qoradev.pythonanywhere.com/")),
        ],
        [
            InlineKeyboardButton(text="Kanalingizga obuna bo'ling", url="https://t.me/hamster_kombat"),

        ],
        [
            InlineKeyboardButton(text="O'yindan qanday olish mumkin", callback_data='odiysoz90')
        ],

    ])
royhatim = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1 bosishda o'ynang 🐹", web_app=WebAppInfo(url="https://qoradev.pythonanywhere.com/")),
        ],
        [
            InlineKeyboardButton(text="Kanalingizga obuna bo'ling", url="https://t.me/hamster_kombat"),

        ],

    ])