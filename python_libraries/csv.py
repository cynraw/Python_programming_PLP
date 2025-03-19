import csv

with open("data.csv", mode='W', newline="") as file:
  writer = csv.writer(file)
  writer.writerow(["name", "age"])
  writer.writerow(["Alice", "23"])
