import pandas as pd
stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)
k = stocks.keys()
v = stocks.values()
df = pd.DataFrame(v, k, ['price'])
print(df)
