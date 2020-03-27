import csv
from collections import namedtuple
from datetime import datetime

data_file = "testing_data/raw_data_testing_sample.csv"


Data = namedtuple("Data", "date_string date_object day_num download upload threads")


def get_speedtest_data(data=data_file):
    data_list = []
    with open(data, encoding="utf-8") as f:
        for line in csv.DictReader(f):
            try:
                date_string = line["date_time_(JST)"]
                date_object = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S")
                day_num = line["day_num"]
                download = line["download"]
                upload = line["upload"]
                threads = line["threads"]
            except ValueError:
                continue
            d = Data(
                date_string=date_string,
                date_object=date_object,
                day_num=day_num,
                download=download,
                upload=upload,
                threads=threads,
            )
            data_list.append(d)
    for entry in data_list:
        print(entry.threads)


if __name__ == "__main__":
    get_speedtest_data()
    # split_data_by_thread()
