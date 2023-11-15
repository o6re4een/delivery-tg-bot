import requests
from config import config


server_url = config.server_api.get_secret_value()
async def get_menu_items():
    r = requests.get(f"{server_url}/food")
    menu_items =  r.json()
    print(menu_items)
    return menu_items

