from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from bot.api.menu_api import get_menu_items

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Блюда"), KeyboardButton(text="Профиль")],


], resize_keyboard=True, input_field_placeholder="Выберите пункт ниже")


profile_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Пополнить"), KeyboardButton(text="Заказы"), KeyboardButton(text="Корзина")],
    [KeyboardButton(text="Главная")]
], resize_keyboard=True)


async def menu():
    menu_kb = InlineKeyboardBuilder()
    menu_items = await get_menu_items()

    for product in menu_items:
        menu_kb.add(InlineKeyboardButton(text=product["name"], callback_data=f'menu_{product["name"]}'))

    menu_kb.add(InlineKeyboardButton(text="Главная", callback_data="Back"))
    return menu_kb.adjust(2).as_markup()