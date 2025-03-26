import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Ronoh'],
    'Age': [23,40,22],
    'Cities': ['Nairobi', 'Kisumu', 'Eldoret']
}

df = pd.DataFrame(data)
print(df)
print(df[df['Age'] > 30]) # filter rows with age > 30
pd.drop('Cities', axis = 1, inplace = 'True')
