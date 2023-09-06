import pandas as pd
url='https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv'
df = pd.read_csv(url, skiprows=range(1, 32))  # Adjust the range as needed


print(df.describe())

df.describe()
def negative(x):
  return -x

