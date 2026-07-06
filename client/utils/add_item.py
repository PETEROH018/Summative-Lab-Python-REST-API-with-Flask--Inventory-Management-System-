import requests
import sys
from colorama import Fore,Style,init
from models.Item import Item
init(autoreset=True)

def add_item(args):
    if args.name == None or args.brands == None or args.code == None:
        print(f"{Fore.RED}All arguments should be supplied!")
        sys.exit(True)

    data = Item(args.name,args.brands,args.code)
    new_item = {
        "product_name": data.name,
        "brands": data.brands,
        "code": data.code
    }

    response = requests.post('http://127.0.0.1:5000/inventory',json=new_item)
    print(f"{Fore.GREEN}{response.json().get("message")}")