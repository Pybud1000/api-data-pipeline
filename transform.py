import pandas as pd
import numpy as np

products = pd.read_csv(r'C:\Users\PCXPC\Documents\super secret hehehe\Projects\api-data-pipeline\staging\products.csv')
reviews = pd.read_csv(r'C:\Users\PCXPC\Documents\super secret hehehe\Projects\api-data-pipeline\staging\reviews.csv')

products = pd.DataFrame(products)
reviews = pd.DataFrame(reviews)

# CLEANING

products['tags'] = products['tags'].str.replace(r"[\[\]']", "", regex=True)

# PROD

products.to_csv(r'C:\Users\PCXPC\Documents\super secret hehehe\Projects\api-data-pipeline\Clean\products.csv', index=False)
reviews.to_csv(r'C:\Users\PCXPC\Documents\super secret hehehe\Projects\api-data-pipeline\Clean\reviews.csv', index=False)

