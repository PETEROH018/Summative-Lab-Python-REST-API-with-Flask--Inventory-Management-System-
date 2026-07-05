import argparse
from utils import view_items,view_item,add_item

def main():
    parser = argparse.ArgumentParser(description="Python-REST-API-with-Flask--Inventory-Management-System-")
    subparsers = parser.add_subparsers()

    view_items_subparser = subparsers.add_parser("view-items",help="view all items in the inventory")
    view_items_subparser.set_defaults(func=view_items)

    view_item_subparser = subparsers.add_parser("view-item",help="view an item's details by specifying its id")
    view_item_subparser.add_argument('--id',help="Provide the id of the item you want to view which should be an integer")
    view_item_subparser.set_defaults(func=view_item)

    add_item_subparser = subparsers.add_parser("add-item",help="Add a new item into the inventory")
    add_item_subparser.add_argument('--name',help="Provide the product name")
    add_item_subparser.add_argument('--brands',help="Provide the brands of the item")
    add_item_subparser.add_argument('--code',help="Provide a 13 digit barcode for the item")
    add_item_subparser.set_defaults(func=add_item)

    args = parser.parse_args()
    if hasattr(args,"func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()