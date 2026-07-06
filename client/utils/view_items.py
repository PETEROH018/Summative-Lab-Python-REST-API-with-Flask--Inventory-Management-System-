import requests

def view_items(args):
    response = requests.get('http://127.0.0.1:5000/inventory')
    items = response.json()
    for item in items:
        print (f'{item.get('id')}. name: {item.get('product_name')}, brands: {item.get('brands')}')