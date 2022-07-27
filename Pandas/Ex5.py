import numpy as np
import pandas as pd
data = np.arange(10,100,10)
index = np.arange(101,110)
df = pd.Series(data,index,dtype="float")
print(df)
