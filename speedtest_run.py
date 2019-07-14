import speedtest
import os
import csv
import datetime
import time

file = "speedtesting_all_threads.csv"

def speedtest_func(threads, file):
    if not os.path.isfile(file):
        headers = [['date_time_(JST)', 'download', 'upload', 'threads']]
        with open(file, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(headers)

    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M:%S")
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
    if threads == None:
        new_row = [current_date_string, download, upload, 'None']
    else:
        new_row = [current_date_string, download, upload, str(threads)]

    with open(file, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_row)


running = True

while running:
    speedtest_func(threads=1, file = file)
    speedtest_func(threads=None, file=file)
    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M")
    print(current_date_string)
    time.sleep(120)