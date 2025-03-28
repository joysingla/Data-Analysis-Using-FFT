import pandas as pd
import numpy as np

df1 = pd.read_csv('SampleData.csv', names=['timestamp', 'acceleration1'])
df2 = pd.read_csv('ReferenceData.csv', names=['timestamp', 'acceleration2'])

merged_df = pd.merge(df1, df2, on='timestamp', how='inner')
merged_df['acceleration_diff'] = np.linalg.norm(merged_df[['acceleration1', 'acceleration2']].values, axis=1)

print(merged_df)
