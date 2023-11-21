import requests
from config import config
import datetime

server_url = config.server_api.get_secret_value()

def create_order(user_id):
    r = requests.post(f'{server_url}/order/{user_id}')
    user_order_data = r.json()
    # print(user_data)
    

    order_data = format_order(user_order_data)

    return order_data


def get_user_orders(user_id):
    r = requests.get(f'{server_url}/order/{user_id}')
    user_order_data = r.json()
    order_data = format_order(user_order_data)

    return order_data

def format_order(data):
    order_info = (
    f"<b>Уникальный номер заказа:</b> {data['id']}\n"
    f"<b>Дата:</b> {data['date']}\n"
    f"<b>Статус:</b> {data['status']}\n"
    f"<b>Цена:</b> ${data['price']}\n"
    
    f"<b>Заказанные продукты:</b>\n"
) 
    for item in data['orderItems']:
        order_info += (
          
            f"    <b>Продукт:</b> {item['food']['name']}\n"
            f"    <b>Количество:</b> {item['quantity']}\n"
            f"    <b>Цена за 1:</b> ${item['food']['price']}\n"
            f"    <b>Всего:</b> ${float(item['quantity']) * float(item['food']['price']):.2f}\n"
          
        )