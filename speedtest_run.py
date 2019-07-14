import speedtest
import os
import csv
import datetime
import time


def speedtest_func(threads, file):
    if not os.path.isfile(file):
        headers = [['date_time_(JST)', 'download', 'upload']]
        with open(file, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(headers)

    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M")
    date_string = date_object.strftime("%d/%m/%y")
    time_string = date_object.strftime("%H:%M")
    servers = []

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()

    download = int(results_dict['download'])
    upload = int(results_dict['upload'])
    new_row = [current_date_string, download, upload]

    with open(file, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_row)


running = True

while running:
    speedtest_func(threads=1, file = "speedtesting_single_thread.csv")
    speedtest_func(threads=None, file="speedtesting_multi_thread.csv")
    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M")
    print(current_date_string)
    time.sleep(300)