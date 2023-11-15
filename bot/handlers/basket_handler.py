from aiogram import Router, F, flags
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.states.states import User_Data
from bot.keyboards.keyboards import main, menu
from bot.api.basket_api import get_user_cart_formated

basket_router = Router()



@basket_router.message(F.text=="Корзина", StateFilter(User_Data.editing_profile_state, User_Data.editing_basket_items))
@flags.chat_action("typing")
async def get_user_basket(
        message: Message,
        state: FSMContext
):
    await state.set_state(User_Data.editing_basket_items)
    
    data = await state.get_data()
    user_id = data["user_id"]

    formatted_cart = await get_user_cart_formated(user_id)
    await message.answer(formatted_cart, parse_mode="html")    

    
    # await message.answer("Выберите продукт", reply_markup=await menu())
