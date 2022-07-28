import pandas as pd
stocks = {'PLW': 387.00, 'CDR': 339.5, 'TEN': 349.5, '11B': 391.0}
quotations = pd.Series(data=stocks)
quotations = quotations.append(pd.Series(pd.Series({'BBT':25.5,'F51':19.2})))
print(quotations)
