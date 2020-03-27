import speedtest
import os
import csv
import datetime
import time

analysis_folder_name = "data_for_analysis"
if not os.path.isdir(analysis_folder_name):
    os.mkdir(analysis_folder_name)
folder_prefix = "current_data"
file = folder_prefix + "/speedtesting_data.csv"
if not os.path.isdir(folder_prefix):
    os.mkdir(folder_prefix)

if not os.path.isfile(file):
    headers = [
        ["date_time_(JST)", "weekday", "day_num", "download", "upload", "threads"]
    ]
    with open(file, "w") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(headers)


def speedtest_func(threads, file):
    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M:%S")
    weekday = date_object.strftime("%A")
    servers = []

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()

    download = int(results_dict["download"])
    upload = int(results_dict["upload"])
    day_num = datetime.datetime.today().weekday()
    if threads == None:
        new_row = [current_date_string, weekday, day_num, download, upload, "None"]
    else:
        new_row = [
            current_date_string,
            weekday,
            day_num,
            download,
            upload,
            str(threads),
        ]

    with open(file, "a") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_row)


running = True

while running:
    try:
        speedtest_func(threads=1, file=file)
    except:
        time.sleep(60)
    try:
        speedtest_func(threads=None, file=file)
    except:
        time.sleep(60)
    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M")
    print(current_date_string)
    time.sleep(120)
