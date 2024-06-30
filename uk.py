import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://results.eci.gov.in/PcResultGenJune2024/partywiseresult-S28.htm'

response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.content, 'html.parser')


resultstable =  soup.find('table', class_="table")
headers_main = resultstable.find_all('th')
headers = [title.text.strip() for title in headers_main][0:4]

df = pd.DataFrame(columns=headers)

column_data = resultstable.find_all('tr')
for row in column_data[1:]:
    row_data = row.find_all('td')
    ird = [data.text.strip() for data in row_data]
    if len(ird) == len(headers):  
        length = len(df)
        df.loc[length] = ird
    

print(df)

df.to_excel('uk.xlsx', index=False)