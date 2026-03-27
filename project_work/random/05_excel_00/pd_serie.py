try:
  import pandas as pd
  import numpy as np
except ImportError:
  print("Pandas library is not installed. Please install it using 'pip install pandas' and try again.")
  exit()

ser = pd.Series()
print("Panda series: ",ser)

data = np.array(['a','b','c','d'])

ser = pd.Series(data)
print("Panda series from numpy array: \n",ser)