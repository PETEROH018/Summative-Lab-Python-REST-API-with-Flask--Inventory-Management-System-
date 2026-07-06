import requests
from colorama import Fore,init,Style
init(autoreset=True)

def view_items(args):
    response = requests.get('http://127.0.0.1:5000/inventory')
    items = response.json()
    for item in items:
        print (f'{Fore.YELLOW}{item.get('id')}{Style.RESET_ALL}. {Fore.GREEN}name{Style.RESET_ALL}: {item.get('product_name')}, {Fore.GREEN}brands{Style.RESET_ALL}: {item.get('brands')}')