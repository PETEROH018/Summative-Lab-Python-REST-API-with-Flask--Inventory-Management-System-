import requests

def get_items():
        url = 'https://world.openfoodfacts.org/api/v2/search'
        params = {"page_size":50,"fields":"code,product_name,brands"}
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
        response = requests.get(url,params=params,headers=headers)
        response.raise_for_status()
        items = [{**item,"id":index+1} for index,item in enumerate(response.json()["products"])]
        return items




