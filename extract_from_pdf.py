import os
# from ..settings import PDF_PATH, CSV_PATH
import camelot
import pandas
from datetime import datetime

BASE_PATH = "c:\\Users\\GGONZALEZ\\Documents\\python source\\covid19bot\\covid19bot\\"
PDF_PATH = os.path.join(BASE_PATH, 'data', 'gobmx', 'pdf')
CSV_PATH = os.path.join(BASE_PATH, 'data', 'gobmx', 'csv')
name = 'gobmx'

filename = "Tabla_casos_positivos_COVID-19_resultado_InDRE_2020.04.01.pdf"
tables = camelot.read_pdf(os.path.join(PDF_PATH, filename), pages="1-end")
print(tables)
print(tables[0])
print(tables[0].parsing_report)
print(tables[0].df)

dataframes = []
for table in tables:
    dataframes.append(table.df)

entire_table = pandas.concat(dataframes)

csv_name = name
if "casos_positivos" in filename:
    csv_name = "casos_positivos"
elif "casos_sospechosos" in filename:
    csv_name = "casos_sospechosos"
csv_name = csv_name+"_data_"+datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".csv"

entire_table.to_csv(os.path.join(CSV_PATH, csv_name))