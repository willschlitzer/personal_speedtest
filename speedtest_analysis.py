import pandas as pd
#from speedtest_run import file

file = "speedtesting_single_thread.csv"

df = pd.read_csv(file, index_col="date_time_(JST)", parse_dates=True)
resampled_df = df.resample('H').mean()
print(resampled_df)