import pandas as pd

def readcols(fileloc, columns):
    data = pd.read_excel(fileloc, usecols=columns, sheet_name="Sheet1", header=None)
    return data.to_numpy().ravel().tolist()

def readingfromexcel(fileloc):
    columns = ["A", "B", "C"]
    column_names = ["H_Unit", "CH1_s", "CH2_s"]
    arrays = {name: readcols(fileloc, col) for name, col in zip(column_names, columns)}
    return arrays

def reads():
    fileloc = "1196.xlsx"
    arrays = readingfromexcel(fileloc)
    return arrays