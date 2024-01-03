import quandl
quandl.ApiConfig.api_key = 'uKsPezNKzKYxk6e8pxRb'

data = quandl.get('WIKI/FB')

print("First ten rows of the dataframe:")
print(data.head(10))

data['Profit'] = data['Close'] - data['Open']

negative_profit_days = len(data[data['Profit'] < 0])
print(f"Number of days with negative profit: {negative_profit_days}")

mean_profit = data['Profit'].mean()
print(f"Mean Profit for the entire data: {mean_profit:.2f}")

print("First 10 rows with columns Open, Close, Profit:")
print(data[['Open', 'Close', 'Profit']].head(10))