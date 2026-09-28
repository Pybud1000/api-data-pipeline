import pandas as pd
import numpy as np
import requests

products_path = r'C:\Users\PCXPC\Documents\super secret hehehe\Projects\api-data-extraction-pipeline\products.csv'
reviews_path = r'C:\Users\PCXPC\Documents\super secret hehehe\Projects\api-data-extraction-pipeline\reviews.csv'

try:
    url = "https://dummyjson.com/products"

    skip = 0
    limit = 30

    products = []
    reviews = []

    while True:
        params = {
            "skip" : skip,
            "limit" : limit
        }

        response = requests.get(
            url,
            params=params
        )

        response.raise_for_status()
        data = response.json()

        product_page = data["products"]
        products.extend(product_page)

        # Reviews Table
        s_reviews = pd.json_normalize(
            data["products"],
            record_path="reviews",
            meta=["id"]
        )
        s_reviews = s_reviews.rename(columns={
            "id" : "product_id"
        })

        reviews.append(s_reviews)

        total = data["total"]

        if len(products) >= total:
            break
        skip += limit

    # Products Table
    products = pd.json_normalize(products)
    products = products.drop(columns=["reviews"])

    reviews = pd.concat(
        reviews,
        ignore_index=True
    )

    products.to_csv(products_path, index=False)
    reviews.to_csv(reviews_path, index=False)

except requests.exceptions.Timeout:
    print("request timed out")
except requests.exceptions.ConnectionError:
    print("Could not connect to server")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.exceptions.JSONDecodeError:
    print("Response was not a valid JSON")
except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")