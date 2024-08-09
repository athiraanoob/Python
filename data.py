import pandas as pd
import numpy as np
url = pd.read_csv('C:\\Users\\athir\\OneDrive\\Documents\\New folder\\Calendar.csv')
url.head(5)
print(url)
url.info()
url.describe()
url.dtypes