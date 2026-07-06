import re
import sys
from colorama import Fore,Style,init
init(autoreset=True)

class Item:
    def __init__(self,name,brands,code):
        self.name = name
        self.brands = brands
        self.code = code

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if re.match(r"^[a-zA-Z0-9 ]+$",value):
            self._name = value
        else:
            print (f"{Fore.RED}The item name should only contain numbers,letters and spaces!")
            sys.exit(1)

    @property
    def brands(self):
        return self._brands
    @brands.setter
    def brands(self,value):
        if re.match(r"^[a-zA-Z0-9, ]+$",value):
            self._brands = value
        else:
            print (f"{Fore.RED}The item brands should only contain numbers,letters,commas and spaces!")
            sys.exit(1)

    @property
    def code(self):
        return self._code
    @code.setter
    def code(self,value):
        if re.match(r"^[0-9]",value):
            if len(value) == 13:
                self._code = value
            else:
                print(f"{Fore.RED} The barcode should be thirteen digits!")
                sys.exit(1)
        else:
            print (f"{Fore.RED} The barcode should only contain digits!")
            sys.exit(1)
