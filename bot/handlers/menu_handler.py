from aiogram import Router, F, flags, types
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.states.states import User_Data
from bot.keyboards.keyboards import main, menu
from bot.api.basket_api import add_to_cart


menu_router = Router()

@menu_router.message(F.text=="Блюда")
@flags.chat_action("typing")
async def get_menu_from_api(
        message: Message,
        state: FSMContext
):
    await state.set_state(User_Data.choosing_food_name)
    await message.answer("Выберите продукт", reply_markup=await menu())


@menu_router.callback_query(F.data.startswith("menu_"), User_Data.choosing_food_name)
async def product_selected(callback: CallbackQuery, state: FSMContext):
    # product_name = message.data.split("_")[1]
    product_name = callback.data.split("_")[1]
    user_data = await state.get_data()
    await state.update_data(chosen_food=product_name)
    try:
        await add_to_cart(user_data["user_id"], product_name)
        await callback.message.answer("Пицца добавленна в корзину", reply_markup=await menu())
    except Exception as e:
        print(e)
    # await state.set_state(User_Data.choosing_count)

    await callback.answer()


@menu_router.callback_query(F.data=="Back", User_Data.choosing_food_name)
async def back_to_main_menu(
        callback: CallbackQuery,
        state: FSMContext
):
    # await state.clear()
    await state.set_state(None)
    # print("State", await state.get_data())
    await callback.message.answer("Основное меню", reply_markup=main)
    await callback.answer()



# def get_counter_keyboard():
#     buttons = [
#         [
#             types.InlineKeyboardButton(text="-1", callback_data="num_decr"),
#             types.InlineKeyboardButton(text="+1", callback_data="num_incr")
#         ],
#         [types.InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
#     ]
#     keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard


# @menu_router.message(User_Data.choosing_count)
# async def cmd_numbers(message: Message,
#                       # state: FSMContext
#                       ):
#
#     await message.answer("Укажите число: 0", reply_markup=get_counter_keyboard())

# async def update_num_text(message: types.Message, new_value: int,):
#
#     await message.edit_text(
#         f"Укажите число: {new_value}",
#         reply_markup=get_counter_keyboard()
#     )

# @menu_router.callback_query(F.data.startswith("num_"))
# async def callbacks_num(callback: CallbackQuery, state: FSMContext):
#     user_data = await state.get_data()
#     print(user_data)
#     count = user_data["chosen_count"]
#     action = callback.data.split("_")[1]
#
#     if action == "incr":
#         user_data[callback.from_user.id] = count+1
#         await update_num_text(callback.message, count+1)
#     elif action == "decr":
#         user_data[callback.from_user.id] = count-1
#         await update_num_text(callback.message, count-1)
#     elif action == "finish":
#         await callback.message.edit_text(f"Итого: {count}")
#
#     await callback.answer()