from aiogram.fsm.state import StatesGroup, State

# class Menu(StatesGroup):
#     choose_state = State()
#     order_state = State()

class User_Data(StatesGroup):

    editing_basket_items = State()
    user_data: dict
    user_id: int
    chosen_food: str
    chosen_count: int = 0
    # order_state = State()
    # menu_state = State()
    editing_profile_state = State()

    # Выбирает блюдо
    choosing_food_name = State()

    # Выбирает количество
    choosing_count =State()

    # Заказывает
    ordering_food = State()

    #Menu state


# class Order_State(StatesGroup):
#
