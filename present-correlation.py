import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
  Roll_No = []
  Percentage = []
  Days_Present = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      Percentage.append(float(row["Marks In Percentage"]))
      Days_Present.append(float(row["Days Present"]))
  return {"x": Percentage, "y": Days_Present}

def find_Correlation(data_source):
  correlation = np.corrcoef(data_source["x"],data_source["y"])
  print("Correlation between Percentage And Days Present spent watching TV in a week (hours) :-\n--->",correlation[0,1])

def setup():
  data_path = "Present.csv"
  data_source = getDataSource(data_path)
  find_Correlation(data_source)

setup()      