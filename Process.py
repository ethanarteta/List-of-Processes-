import os
import psutil
import csv

# This python code makes a csv file with a list of all processes info along with the resources used 

process_list = []
# Iterate through all running processes and it retrieves information about each process
for process in psutil.process_iter(['pid', 'name', 'exe', 'cpu_percent', 'memory_info']):
    try:
        process_info = process.info
        process_list.append(process_info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
# print(process_list)

# Make the CSV file path
csv_file = "process_list.csv"

# Make the CSV column headers
csv_columns = ["PID", "Name", "Executable Path", "CPU Usage (%)", "Memory Usage (bytes)"]


rows = [
    {
        "PID": process["pid"],
        "Name": process["name"],
        "Executable Path": process["exe"],
        "CPU Usage (%)": process["cpu_percent"],
        "Memory Usage (bytes)": process["memory_info"].rss
    }
    for process in process_list
]

with open(csv_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(rows)


print(f"Process list saved to {csv_file}")




