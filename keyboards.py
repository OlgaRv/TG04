from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
    [KeyboardButton(text="Кнопка 3")]
], resize_keyboard=True)

inline_keyboard_test = InlineKeyboardMarkup(inline_keyboard=[
#    [InlineKeyboardButton(text="Видео", url="https://www.youtube.com/watch?v=HfaIcB4Ogxk")],
    [InlineKeyboardButton(text="Каталог", callback_data="catalog")],
    [InlineKeyboardButton(text="Новости", callback_data="news")],
    [InlineKeyboardButton(text="Профиль", callback_data="person")]
])

test = ['элемент 1', 'элемент 2', 'элемент 3', 'элемент 4']

async def test_keyboard():
    keyboard = ReplyKeyboardBuilder()
    for key in test:
        keyboard.add(KeyboardButton(text=key))
    return keyboard.adjust(2).as_markup()

async def test_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    for key in test:
        keyboard.add(InlineKeyboardButton(text=key, url='https://www.youtube.com/watch?v=HfaIcB4Ogxk'))
    return keyboard.adjust(2).as_markup()