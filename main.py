import pandas as pd
url='https://gist.github.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea'
df = pd.read_csv(url)

print(df.describe())

df.describe()
def negative(x):
  return -x

