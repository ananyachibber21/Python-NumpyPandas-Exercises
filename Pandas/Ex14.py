import pandas as pd
date_range = pd.date_range(start="2021-03-01", periods = 31)
df = pd.DataFrame(date_range, columns=['day'])
df['day_of_year'] = df['day'].dt.dayofyear
print(df)
