
import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"
response = requests.get(url) # bütün veriler burada 

html_icerigi = response.content # web sitesinin html içeriğine erişiyoruz
soup = BeautifulSoup(html_icerigi,"html.parser") # web sitesini parçalamak istediğimizi söylüyoruz
rt = float(input("Rating giriniz: "))


"""
for i in soup.find_all("td",{"class":"titleColumn"}): #burada sadece film isimlerinin bulunduğu yeri alıyoruz
    print(i.text) #burada sadece yazıları alıyoruz 
    print("***********************************************")
"""
basliklar = soup.find_all("td",{"class":"titleColumn"})
rating = soup.find_all("td",{"class":"ratingColumn imdbRating"})

for baslik, rating in zip(basliklar,rating):
    baslik = baslik.text
    rating = rating.text

    baslik = baslik.strip()
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n","")

    if (float(rating) > rt):
        print("Film ismi: {}\nFilmin Ratingi : {}\n".format(baslik,rating))