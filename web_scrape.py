years = list(range(2018, 2025))

url_start = "https://www.basketball-reference.com/awards/awards_{}.html"

import requests

for year in years:
    url = url_start.format(year)
    data = requests.get(url)

    with open("mvps/{}.html", format(year), "w+") as f:
              f.wriite(data.text)