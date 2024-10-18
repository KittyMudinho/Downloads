from bs4 import BeautifulSoup
import requests
import openpyxl
from openpyxl.chart import BarChart,Reference
url="https://www.google.com/search?q=weatherSantos"
html = requests.get(url).content
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
tempInt=temp.split("°")
tempetura=tempInt[0]
data = str.split('\n')
time = data[0]
print(f"Temperatura:{tempetura}\nData e hora:{time}")
try:
    wb=openpyxl.load_workbook('Test.xlsx')
    ws=wb.active
    ws.append([int(tempetura),time])
except:
    wb=openpyxl.Workbook()
    ws=wb.active
    ws['A1']=int(tempetura)
    ws['B1']=time
if ws._charts:
    ws._charts.clear()
chart=BarChart()
chart.title =  "Temperatura e horário"
chart.y_axis.title = "Temperatura"
chart.x_axis.title = "Horário"
linhas = len([row for row in ws if not all([cell.value == None for cell in row])])
data=Reference(
    ws,
    min_col=1,
    min_row=1,
    max_col=2,
    max_row=linhas
)
cats = Reference(ws, min_col=2, min_row=1, max_row=linhas)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)
chart.legend=None
ws.add_chart(chart,"H2")
wb.save('Test.xlsx')