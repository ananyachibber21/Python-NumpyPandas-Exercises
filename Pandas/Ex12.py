import pandas as pd
datetimeIndex = pd.date_range(start='2020-01-01', periods=52, freq='W-MON')
print(datetimeIndex)
