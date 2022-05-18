import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url) #we pulled the information, all the information in it

html_icerigi = response.content # This is how we access the html content.
soup = BeautifulSoup(html_icerigi,"html.parser") #

"""
for i in soup.find_all("div") : # returns a list with div tags
    print(i)
    print("****************************************")
"""

print(soup.find_all("div", {"class": "yp-poi-box-2"})) # we only get certain part of divs
