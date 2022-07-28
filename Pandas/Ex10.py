import pandas as pd
dict = {
    'company':['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.0,178.6,179.2],
    'ticker': ['AMZN.US', 'MSFT.US','FB.US']
}
companies = pd.DataFrame(dict)
print(companies)
