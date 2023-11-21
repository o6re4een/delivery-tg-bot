from aiogram import Router, F, flags
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.api.order_api import create_order, get_user_orders
from bot.states.states import User_Data
from bot.keyboards.keyboards import main, menu
from bot.api.basket_api import get_user_cart_formated

order_router = Router()



@order_router.message(F.text=="Заказы", StateFilter(User_Data.editing_profile_state))
@flags.chat_action("typing")
async def get_user_basket(
        message: Message,
        state: FSMContext
):
    await state.set_state(User_Data.editing_profile_state)
    
    data = await state.get_data()
    user_id = data["user_id"]

    formatted_order = await get_user_orders(user_id)
    await message.answer(formatted_order, parse_mode="html")    

    
    # await message.answer("Выберите продукт", reply_markup=await menu())
