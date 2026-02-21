import csv

def log_data(lat, lon, gas):
    with open('log_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([lat, lon, gas])