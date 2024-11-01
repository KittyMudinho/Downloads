from bs4 import BeautifulSoup
import pandas as pd
import datetime
import requests
import openpyxl
from openpyxl.chart import BarChart,Reference
import plotly.express as px
cidade=input('Diga a cidade que deseja saber a temperatura (Say the city you wish to know the temperature): ')
url=f'https://www.google.com/search?q=weather{cidade}'
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = (soup.find('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'}).text.split('°C')[0].split('de ')[1])
time = datetime.datetime.now()
print(f"Temperatura:{temp}°C\nData e hora:{time}")
try:
    wb=openpyxl.load_workbook('Test.xlsx')
    ws=wb.active
    ws.append([int(temp),time])
except:
    wb=openpyxl.Workbook()
    ws=wb.active
    ws['A1']='temperatura'
    ws['A2']=int(temp)
    ws['B1']='Horário'
    ws['B2']=time
wb.save('Test.xlsx')
arquivo=pd.read_excel('Test.xlsx')
grafico=px.bar(arquivo,x='Horário', y='temperatura')
grafico.show()
