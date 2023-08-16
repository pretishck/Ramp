import pandas as pd
df=pd.read_csv('sample data.csv')
df['transaction_time'] = pd.to_datetime(df['transaction_time'])

# Sort by timestamp
df = df.sort_values(by='transaction_time')

df['date']=df['transaction_time'].dt.date
soln=df.groupby('date')['transaction_amount'].sum().reset_index()
print(soln['transaction_amount'].astype(float).rolling(3).mean()[30])
