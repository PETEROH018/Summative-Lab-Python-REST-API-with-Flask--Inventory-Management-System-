import requests
import re
from colorama import Fore,Style,init
init(autoreset=True)

# This function is used to view an item's details where the item is selected by id by making a GET request to the server
def view_item(args):
    if args.id != None:
        if re.match(r"^[0-9]+$",args.id):
            response = requests.get(f'http://127.0.0.1:5000/inventory/{args.id}')
            item = response.json()
            if "error" in item:
                print(f"{Fore.RED}{item.get("error")}")
            else:
                print(f"{Fore.GREEN}id{Style.RESET_ALL}: {item.get("id")} \n{Fore.GREEN}name{Style.RESET_ALL}: {item.get("product_name")}\n{Fore.GREEN}brands{Style.RESET_ALL}: {item.get("brands")} \n{Fore.GREEN}barcode{Style.RESET_ALL}: {item.get("code")}")
        else:
            print(f"{Fore.RED}Please enter an integer id!")
    else:
        print(f"{Fore.RED}Please include an item id in the argument!")    
