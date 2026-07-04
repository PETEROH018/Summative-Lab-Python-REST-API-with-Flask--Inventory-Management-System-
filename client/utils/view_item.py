import requests
from colorama import Fore,Style,init
init(autoreset=True)

def view_item(args):
    try:
        id = int(input("Enter the id of the item you want to view: "))
        response = requests.get(f'http://127.0.0.1:5000/inventory/{id}')
        item = response.json()
        if "error" in item:
            print(f"{Fore.RED}{item.get("error")}")
        else:
            print(f"{Fore.GREEN}id{Style.RESET_ALL}: {item.get("id")},{Fore.GREEN}name{Style.RESET_ALL}: {item.get("product_name")},{Fore.GREEN}brands{Style.RESET_ALL}: {item.get("brands")}")
    except ValueError as e:
        print(f"{Fore.RED}Please enter an integer id!")
        view_item(args)
    
