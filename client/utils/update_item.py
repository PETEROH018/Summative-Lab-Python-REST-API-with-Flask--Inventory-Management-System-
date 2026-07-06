from colorama import Fore,init,Style
import re
import requests
import sys
init(autoreset=True)

# This function handles updating an item's details such as the name and brands by making a PATCH request to the server
# The if statements are used to validate inputs and to ensure only the values that need to be changed are changed
def update_item(args):
    if args.brands == None and args.name == None:
        print(f"{Fore.RED} Provide at least one value to update!{Style.RESET_ALL}{Fore.GREEN} Either the name or brands")
        sys.exit(1)
    elif args.brands == None:
        if re.match(r"^[a-zA-Z0-9 ]+$",args.name):
            item_update = {"product_name":args.name}
        else: 
            print (f"{Fore.RED}The item name should only contain numbers,letters,commas and spaces!")
            sys.exit(1)
    elif args.name == None:
        if re.match(r"^[a-zA-Z0-9, ]+$",args.brands):
            item_update = {"brands":args.brands}
        else:
            print (f"{Fore.RED}The item brands should only contain numbers,letters,commas and spaces!")
            sys.exit(1)
    else:
        if not re.match(r"^[a-zA-Z0-9 ]+$",args.name):
            print (f"{Fore.RED}The item name should only contain numbers,letters,commas and spaces!")
            sys.exit(1)
        if not re.match(r"^[a-zA-Z0-9, ]+$",args.brands):
            print (f"{Fore.RED}The item brands should only contain numbers,letters,commas and spaces!")
            sys.exit(1)
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