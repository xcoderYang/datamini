import pandas as pd

titleLength = 5
article = 10
data = pd.read_csv('../emotion/train/Train_DataSet.csv')
print(data.loc[::1,:])