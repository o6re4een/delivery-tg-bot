from aiogram import Router, F, flags
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from bot.states.states import User_Data
from bot.keyboards.keyboards import main, menu, profile_keyboard
from bot.api.user_api import create_user

router = Router()

# available_food_sizes = ["Маленькую", "Среднюю", "Большую"]


@router.message( CommandStart())
async def cmd_start(message: Message, state: FSMContext):

    user_data = await create_user(message.from_user.id)
    await state.update_data(user_data = user_data)
    await state.update_data(user_id = user_data["id"])
    await state.update_data(balance=user_data["balance"] if user_data["balance"] else 0)

    # print("Data: ", data)
    await message.answer(f"Вас привествует сервис доставки", reply_markup=main)



@router.message(F.text=="Профиль",)
@flags.chat_action("typing")
async def get_user_data(
        message: Message,
        state: FSMContext
):

    data = await state.get_data()
    await message.answer(text=f" {data}")
    await message.answer("Редактирование профиля", reply_markup=profile_keyboard)
    await state.set_state(User_Data.editing_profile_state)


@router.message(F.text=="Пополнить", User_Data.editing_profile_state)
@flags.chat_action("typing")
async def get_user_data(
        message: Message,
        state: FSMContext
):
    data = await state.get_data()
    await message.answer(text=f" {data}")
    await message.answer("Редактирование профиля", reply_markup=profile_keyboard)
    await state.set_state(User_Data.editing_profile_state)



@router.message(F.text=="Главная",)
@flags.chat_action("typing")
async def back_to_main_menu(
        message: Message,
        state: FSMContext
):
    await message.answer("Основное меню", reply_markup=main)
    await state.set_state(None)
    # data = await state.get_data()
    # await message.answer(text=f" {data}")
    # await message.answer("Редактирование профиля", reply_markup=profile_keyboard)
    # await state.set_state(User_Data.editing_profile_state)
    #
    # await callback.message.answer("Основное меню", reply_markup=main)
    # await callback.answer()


