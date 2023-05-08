import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/8/html/configuration_reference_guide/firewalls-default-ports"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
table = soup.find("table")
headers = [th.text.strip() for th in table.findAll("th")]
rows = []

for tr in table.findAll("tr"):
    row = [td.text.strip() for td in tr.findAll("td")]
    if row:
        rows.append(row)

df = pd.DataFrame(rows, columns=headers)
df.to_excel("ports_data.xlsx", index=False)
