import requests
from config import config


server_url = config.server_api.get_secret_value()

async def add_to_cart(user_id: str, food_name: str):
    r = requests.post(f"{server_url}/basket/add", data={
        "user_ID": user_id,
        "foodName": food_name
    })
    
    basket =  r.json()
    formated_basket = format_basket(basket)
    # print(basket)
    return formated_basket

async def get_user_cart_formated(user_id: str):
    r = requests.get(f"{server_url}/basket/{user_id}")
    basket = r.json()
    formated_basket = format_basket(basket)
    # print(basket)
    return formated_basket


def format_basket(cart_data):
    formatted_text = f"<b>Корзина:</b>\n"

    for item in cart_data['foods']:
        formatted_text += f"------------------- \n <b>{item['name']}</b> \n Количество: {item['quantity']} шт \n Цена: {item['price']} RUB за штуку \n " \
                          f"<b>Сумма:</b> {item['totalPrice']} RUB \n"

    formatted_text += f"------------------- \n <b>Итого: {cart_data['price']} RUB </b> \n"
    return formatted_text

