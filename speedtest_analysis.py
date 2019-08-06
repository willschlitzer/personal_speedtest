import pandas as pd
import matplotlib.pyplot as plt

file = "data_for_analysis/speedtesting_all_threads_19Jul19.csv"

df = pd.read_csv(file, index_col="date_time_(JST)", parse_dates=True)
resampled_df = df.resample("H").mean().dropna()
#print(resampled_df)
resampled_df.plot()
plt.show()
