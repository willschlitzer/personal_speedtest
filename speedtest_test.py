import speedtest
import os
import csv
import datetime
import time

file = "speedtesting.csv"

if not os.path.isfile(file):
    headers = [['date', 'time(JST)','download', 'upload']]
    with open(file, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(headers)

running = True

while running:
    date_object = datetime.datetime.now()
    current_date_string = date_object.strftime("%d/%m/%y %H:%M")
    date_string = date_object.strftime("%d/%m/%y")
    time_string = date_object.strftime("%H:%M")
    servers = []
    # If you want to test against a specific server
    # servers = [1234]

    threads = 1
    # If you want to use a single threaded test
    # threads = 1

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    results_dict = s.results.dict()

    download = int(results_dict['download'])
    upload = int(results_dict['upload'])
    new_row = [date_string, time_string, download, upload]

    with open(file, 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(new_row)
    print(current_date_string)
    time.sleep(300)