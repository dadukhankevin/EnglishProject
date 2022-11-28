import requests as r
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from textblob import TextBlob
from time import sleep
from matplotlib import pyplot as plt
options = webdriver.EdgeOptions()
options.add_argument("--enable-javascript")
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
term = "phone"
year = 2019
go = 1
sentiment = []
all = []
i = 1
while go:
    l = 0
    year += 1
    for i in range(3):
        driver.get("https://www.wsj.com/search?query={q}&isToggleOn=true&operator=OR&sort=relevance&duration=1y&startDate={year}%2F01%2F01&endDate={year}%2F12%2F30&meta=&source=wsjie&page={page}".format(q=term, year=str(year), page=i+1))
        i += 1
        sleep(.5)
        sent = 0
        html = driver.page_source
        html = BS(html).findAll("span", {"class": "WSJTheme--summaryText--2LRaCWgJ"})
        l += len(html)
        for i in html:
            sent += TextBlob(i.text).polarity
    print(l)
    try:
        sent = sent/l
    except:
        continue
    with open(term + str(year) + ".txt", "w+") as f:
        all.append(sent)
        f.write(str(str(sent)))
    print(year)
    if year == 2022:
        input(all)
        plt.plot(all)
        plt.show()
        input("done")
        plt.savefig("currency.png")

