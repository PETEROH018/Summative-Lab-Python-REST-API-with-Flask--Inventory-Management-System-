import requests

# This function handles fetching inventory data from the OpenFoodFacts API
# Since the API often responds with status code 503, recursion is used untill a successful response and the data are obtained
def get_items():
        url = 'https://world.openfoodfacts.org/api/v2/search'
        params = {"page_size":50,"fields":"code,product_name,brands"}
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
        response = requests.get(url,params=params,headers=headers)
        if response.ok:
            items = [{**item,"id":index+1} for index,item in enumerate(response.json()["products"])]
            return items # The items are assigned a unique id and packaged into a python list before being returned for use in app.py
        else:
            get_items()




