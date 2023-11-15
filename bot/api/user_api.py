import requests
from config import config


server_url = config.server_api.get_secret_value()
async def create_user(telegram_id):
    r = requests.post(f'{server_url}/users', data={
        "telegram_ID": telegram_id
    })
    user_data = r.json()
    # print(user_data)
    return user_data