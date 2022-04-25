#from selenium import webdriver
from bs4 import BeautifulSoup as bs4
import requests
import csv
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
#browser = webdriver.Chrome("./chromedriver")
#browser.get(START_URL)

page=requests.get(START_URL)
print(page)
soup=bs4(page.text,'html.parser')
star_table = soup.find('table')

temp_list=[]
table_rows=star_table.find_all('tr')
for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip()for i in td]
    temp_list.append(row)

Declination=[]
Distance=[]
Mass=[]
Radius=[]


for i in range(1,len(temp_list)):
    Declination.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    

df2=pd.DataFrame(list(zip(Declination,Distance,Mass,Radius)),columns=['Declination','Distance','Mass','Radius'])
print(df2)  
df2.to_csv('dwarf_stars.csv')  

