import pandas as pd
#from speedtest_run import file

file = "speedtesting_datetest.csv"

df = pd.read_csv(file, parse_dates=True)
print(df)