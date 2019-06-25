from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.sports-reference.com/cfb/schools/iowa/2018-schedule.html"
page = urlopen(url).read()

soup = BeautifulSoup(page, features="lxml")

cell = soup.find("td",{"data-stat": "Final"})
a = cell.text.strip().encode()
text = a.decode("utf-8")
print("Iowa finished ranked: " + text)