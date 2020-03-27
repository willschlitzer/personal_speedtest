import pandas as pd
import matplotlib.pyplot as plt

file = "data_for_analysis/speedtesting_all_threads_19Jul19.csv"

df = pd.read_csv(file, index_col="date_time_(JST)", parse_dates=True)
df_single = df[df["threads"] == "1"]
df_multi = df[df["threads"] == "None"]
resampled_df = df.resample("H").mean()
# print(resampled_df)
df_single_rhourly = df_single.resample("H").mean().dropna()
# print(df_single_rhourly)
df_single_rhourly.plot()
plt.show()
