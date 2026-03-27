try:
  import pandas as pd
except ImportError:
  print("Pandas library is not installed. Please install it using 'pip install pandas' and try again.")
  exit()

df = pd.DataFrame()
print("Panda DataFrame: \n",df)
data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print("Panda DataFrame from dictionary: \n",df)