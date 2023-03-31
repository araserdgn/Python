from bs4 import BeautifulSoup
import json
import re
import emoji
from urllib.request import Request, urlopen

URL = "https://www.instagram.com/"  # Değişmeyen URL


def verileri_al(kullanici_adi):
    son_url = URL + kullanici_adi

    request = Request(son_url, headers={'User-Agent': 'Mozilla/5.0'})
    # HTML sayfasının kodları geldi bu sayede
    html_verisi = urlopen(request).read()

    soup=BeautifulSoup(html_verisi, 'html.parser')

    veri=soup.find("meta",property="og:description").attrs['content'] # HTML deki verileri aldık. property TAKİPÇİ,GÖNDERİ kısmını aldırır bize
                                                                       #Content ile de içerisindeki değerleri alabildik
    script_etiketi = soup.find('script', {'type': 'application/ld+json'})   # Biyografi için arama yapma yeri     

    veri1 = script_etiketi.contents[0]
    veri1 = re.sub('[^\x00-\x7F]+', '', veri1)  # Emoji sembollerini çıkarma
    data = json.loads(veri1)
    description = data['description']

    description = emoji.demojize(description) # Gereksiz yazıları kaldırdık, direkt biyografi Temel yazılarına ulastık
                                                    
    veri=veri.split("-")[0]          

    veri=veri.split(" ")     

    print("Takipçi sayısı: "+veri[0])                                                  
    print("Takip Edilen sayısı: "+veri[2])                                                  
    print("Gönderi sayısı: "+veri[4])  
    print("Biyografisi: "+description) 

kullanici_adi=input("Kullanıcı adı giriniz: ")
verileri_al(kullanici_adi)
