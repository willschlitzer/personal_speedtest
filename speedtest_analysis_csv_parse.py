import csv
from collections import namedtuple
from datetime import datetime
from time import time
import statistics

# For testing
data_file = "testing_data/raw_data_testing_sample.csv"
# For analysis
# data_file = "data_for_analysis/speedtesting_data_26mar20.csv"

Data = namedtuple(
    "Data", "date_string date_object day_name day_num download upload threads"
)


def main():
    s = time()
    speedtest_data = get_speedtest_data()
    single_thread_data, multi_thread_data = thread_data(data=speedtest_data)
    av_download_dict, av_upload_dict = hourly_grouping(data=single_thread_data)
    print(time() - s)


def thread_data(data):
    """Takes speed data that is includes both single- and multi-threaded data and separated them"""
    single_thread_data = []
    multi_thread_data = []
    for item in data:
        if item[6] == "1":
            single_thread_data.append(item)
        else:
            multi_thread_data.append(item)
    return single_thread_data, multi_thread_data


def get_speedtest_data(data=data_file):
    """Parses csv file with speedtest data and creates list of namedtuples"""
    data_list = []
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                date_string = line["date_time_(JST)"]
                date_object = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S")
                day_name = line["weekday"]
                day_num = line["day_num"]
                download = line["download"]
                upload = line["upload"]
                threads = line["threads"]
            except ValueError:
                continue
            d = Data(
                date_string=date_string,
                date_object=date_object,
                day_name=day_name,
                day_num=day_num,
                download=download,
                upload=upload,
                threads=threads,
            )
            data_list.append(d)
    return data_list


def return_dict_of_lists(start=0, end=24):
    """Creates dictionary with integers as keys and empty lists as values"""
    new_dict = {}
    for i in range(start, end):
        new_dict[i] = []
    return new_dict


def hourly_grouping(data):
    """Creates dictionaries that group data by hour;
    returns dictionaries with hourly averages"""
    start = 0
    end = 24
    download_dict = return_dict_of_lists(start=start, end=end)
    upload_dict = return_dict_of_lists(start=start, end=end)

    for item in data:
        hour = int(item[1].hour)
        download, upload = int(item[4]), int(item[5])
        download_dict[hour].append(download)
        upload_dict[hour].append(upload)
    av_download_dict = get_average_speeds(data_dict=download_dict, start=start, end=end)
    av_upload_dict = get_average_speeds(data_dict=upload_dict, start=start, end=end)
    return av_download_dict, av_upload_dict


def get_average_speeds(data_dict, start, end):
    """Takes a dictionary with int as keys; returns average values for the lists"""
    avg_dict = return_dict_of_lists(start=start, end=end)
    for i in range(start, end):
        data = data_dict[i]
        av_data = int(statistics.mean(data))
        avg_dict[i] = av_data
    return avg_dict


if __name__ == "__main__":
    main()
