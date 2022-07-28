import pandas as pd
data_dict = {
    'company': ['Amazon', 'Microsoft', 'Facebook'],
    'price': [2375.00, 178.6, 179.2],
    'ticker': ['AMZN.US', 'MSFT.US', 'FB.US']
}
companies = pd.DataFrame(data=data_dict)
companies = companies.set_index('company')
print(companies)
