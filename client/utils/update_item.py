from colorama import Fore,init,Style
import re
import requests
import sys

init(autoreset=True)
def update_item(args):
    if args.brands == None and args.name == None:
        print(f"{Fore.RED} Provide at least one value to update!{Style.RESET_ALL}{Fore.GREEN} Either the name or brands")
        sys.exit(1)
    elif args.brands == None:
        item_update = {"product_name":args.name}
    elif args.name == None:
        item_update = {"brands":args.brands}
    else:
        item_update = {
        "product_name":args.name,
        "brands":args.brands
        }
    if args.id != None:
        if re.match(r"^[0-9]+$",args.id):
            response = requests.patch(f"http://127.0.0.1:5000/inventory/{args.id}",json=item_update)
            if "error" in response.json():
                print(f"{Fore.RED}{response.json()["error"]}")
            else:
                print(f"{Fore.GREEN}{response.json()["message"]}")
        else:
            print(f"{Fore.RED}Please enter an integer id!")
    else:
        print(f"{Fore.RED}Please include an item id in the arguments!")