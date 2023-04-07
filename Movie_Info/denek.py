import requests # HTTP ile weblerden veri almak için kullanılır
from bs4 import BeautifulSoup # Veri ayrıştırmak ve çıkarmaya yarar
#* Beauit => gelen yanıtın HTML içeriğini alır
def film_top(film_top_n):
    ana_url=(f"https://www.imdb.com/search/title?title_type="
            f"feature&sort=num_votes,desc&count={film_top_n}")
    kaynak=BeautifulSoup(requests.get(ana_url).content, "html.parser") #Gelen yanıtı parser ayrıştırıcı ile aldık
    for film in kaynak.findAll("div",  class_="lister-item mode-advanced"):
        print("\n Filmin Adı = " + film.h3.a.text) # Filmin adı
        print("Filmin türleri = ",film.find("span",attrs={"class":"genre"}).text) #Türüne ulastık
        print("Filmin Reytingi = ",film.strong.text) # Web sayfadaki strong içindeki yazıyı aldık , Reyting bu da
        print(f"Film hakkında detaylı bilgi için = https://www.imdb.com{film.a.get('href')}") # Filmin linkini aldık
        print("//"*10)

if __name__=="__main__":        
    n = int(input("Kaç tane film izlemek istersin ? "))
    film_top(n)