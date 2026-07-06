# Operation
- This application has two parts, the client and the server
## Server
- To start the server, navigate to the server directory and run "python3 app.py" on the terminal
- This will run a Flask app an provide the server URL which is used by the client to make requests and obtain responses
## Client
- The client is a CLI tool which makes request to the server you started earlier by executing the commands listed below
- For the application to work, the server must be started first before any requests are made by the client
- To make a request on the client, navigate to the client directory and execute a command by running "python3 main.py view-item --id 1" on the terminal
- To view all commands and what each does, run "python3 main.py --help" on the terminal
- To view the arguments of each command, run "python3 main.py add-item --help" on the terminal

# Commands
1. view-items
    - This command is used to view all items in the inventory
    - It does not take any argumemts

2. view-item --id 1
    - This command is used to view the details of a particular item
    - It takes one argument which is the integer id of the item
    - If no id argument is given, an error is displayed indicating "Please include an item id in the argument!"
    - If an id is given which is not an integer, an error is displayed indicating "Please enter an integer id!"

3. add-item --name noodles --brands indomie --code 1234567891234
    - This command is used to add a new item into the inventory
    - It takes three mandatory arguments ie, name,brands,code
    - The name only accepts numbers,letters and spaces and supplying a name with other characters will raise an error indicating "The item name should only contain numbers,letters and spaces!"
    - The brands only accepts numbers,letters,spaces and commas. Supplying brands with other characters will raise an error indicating "The item brands should only contain numbers,letters,commas and spaces". You can list several brand by enclosing them in quotes and separating them with commas e.g., "Nuttela,Zesta"
    - The code only accepts a numnber with exactly 13 digits. If not the case, errors are displayed indicating " The barcode should only contain digits!" or " The barcode should be thirteen digits!"
    - Failing to provide one of the arguments will raise an error indicating "All arguments should be supplied!"
    - On successful addition of an item into the inventory, a success message is displayed indicating "Peanut Butter has been succesfully added to the inventory list"

4. update-item --id 1 --name spaghetti --brands SantaLucia
    - This command is used to update the details of an item
    - It takes a mandatory id argument and two optional arguments, name and brands
    - The id should be an integer, otherwise an error is displayed indicating "Please enter an integer id!"
    - At least one of the arguments between name and brands should be supplied, otherwise an error is displyed indicating "Provide at least one value to update! Either the name or brands"
    - The new item name should only contain numbers, letters and spaces. Otherwise an error is thrown indicating "The item name should only contain numbers,letters,commas and spaces!"
    - The new brands should only contain numbers, letters, spaces and commas. Otherwise an error is thrown indicating "The item brands should only contain numbers,letters,commas and spaces!"
    - On successful update of an item, a success message is shown indicating "Peanut Butter has been updated successfully"

5. remove-item --id 1
    - This command is used to remove an item selected by id from the inventory
    - It takes one argument which is the integer id of the item
    - If no id argument is given, an error is displayed indicating "Please include an item id in the argument!"
    - If an id is given which is not an integer, an error is displayed indicating "Please enter an integer id!"
    - On successful removal of an item, a success message is shown indicating "Peanut Butter has been deleted successfully"
