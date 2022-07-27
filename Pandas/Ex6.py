import pandas as pd
series = pd.Series(['001', '002', '003', '004'], list('abcd'))
series = pd.to_numeric(series)
print(series)
