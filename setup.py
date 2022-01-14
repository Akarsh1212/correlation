import csv
import numpy as np
import plotly.express as px

def plotfigure(data_Path):
    with open (data_Path) as csv_file :
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x = "Days Present", y = "Marks In Percentage")
        fig.show()

def getDataSource (data_Path):
    marks_in_pecentage = []
    days_present = []
    with open (data_Path) as csv_file : 
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_pecentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
    return{"x" : marks_in_pecentage,"y" : days_present}
def find_corelation (dataSource):
    corelation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Corealation : " , corelation[0,1])
def setup():
    data_Path = "Marks.csv"
    dataSource = getDataSource(data_Path)
    find_corelation (dataSource)
    plotfigure(data_Path)
setup()
