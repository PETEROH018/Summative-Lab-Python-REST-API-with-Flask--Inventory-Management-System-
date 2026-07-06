import requests
import re
from colorama import Fore,init
init(autoreset=True)

def remove_item(args):
    if args.id != None:
        if re.match(r"^[0-9]+$",args.id):
            response = requests.delete(f"http://127.0.0.1:5000/inventory/{args.id}")
            if "error" in response.json():
                print(f"{Fore.RED}{response.json()["error"]}")
            else:
                print(f"{Fore.GREEN}{response.json()["message"]}")
        else:
            print(f"{Fore.RED}Please enter an integer id!")
    else:
        print(f"{Fore.RED}Please include an item id in the arguments!")