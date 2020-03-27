import csv
from collections import namedtuple

data_file = "testing_data/raw_data_testing_sample.csv"
single_thread_file = "testing_data/single_thread_testing_sample.csv"
multi_thread_file = "testing_data/multi_thread_testing_sample.csv"

Data = namedtuple
def get_speedtest_data(data=data_file):
    with open(data, encoding="utf-8") as f:
        for line in csv.reader(f):
            print(line)

def split_data_by_thread(data=data_file, multi=multi_thread_file, single=single_thread_file):
    with open(data, encoding="utf-8") as f:
        for line in csv.reader(f):
            if line[5] == '1':
                write_to_csv(file=single, line=line)
            else:
                write_to_csv(file=multi, line=line)

def write_to_csv(file, line):
    with open(file, encoding="utf-8") as f:
        write_line = csv.writer(f)
        write_line.writerow(line)


if __name__ == "__main__":
    #get_speedtest_data()
    #split_data_by_thread()