import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

years = list(range(2018, 2025))

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open("mvp/{}.html".format(year), "w+", encoding="utf-8") as f:
              f.write(data.text)

with open("mvp/2018.html", encoding="utf-8") as f:
       page = f.read()

soup = BeautifulSoup(page, "html.parser")

soup.find('tr', class_="over_header").decompose() # removing header row element

mvp_table = soup.find_all(id="mvp")

dfs = []
for year in years:
    with open("mvp/{}.html".format(year), encoding="utf-8") as f:
        page = f.read()
    soup = BeautifulSoup(page, "html.parser")
    soup.find('tr', class_="over_header").decompose()
    mvp_table = soup.find_all(id="mvp")
    mvp = pd.read_html(StringIO(str(mvp_table)))[0] # dataframe of year mvp voting

    dfs.append(mvp)

print(dfs)