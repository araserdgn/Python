import random as rnd

kartlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',
           1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A',]
oyuncuKartları = []
kurpiyeKartları = []
toplam = 0


def oyuncu():
    while True:
        for i in range(2):
            sec = rnd.choice(kartlar)
            oyuncuKartları.append(sec)
        break
    print(f"Oyuncuya çıkan kartlar = {oyuncuKartları}")


def kurpiye():
    while True:
        for i in range(2):
            sec = rnd.choice(kartlar)
            kurpiyeKartları.append(sec)
        break
    print(f"Kurpiyenin çektiği kartlar = {kurpiyeKartları}")


class islem:
    def __init__(self, kartlar):
        self.kartlar = kartlar

    def toplam(self):
        toplam = 0
        for kart in self.kartlar:
            if kart == 'J' or kart == 'Q' or kart == 'K':
                toplam += 10
            elif kart == 'A':
                toplam += 11
            else:
                toplam += int(kart)
        return toplam

    def kartCek(self):
        cek = rnd.choice(kartlar)
        oyuncuKartları.append(cek)
        return oyuncuKartları

    def kartCekKurpi(self):
        cek = rnd.choice(kartlar)
        kurpiyeKartları.append(cek)
        return oyuncuKartları


oyuncu()
kurpiye()

playerTotal = islem(oyuncuKartları)
dealeTotal = islem(kurpiyeKartları)

if dealeTotal.toplam() < 21:
    cek = dealeTotal.kartCekKurpi()
    if dealeTotal.toplam() >= 21:
        kurpiyeKartları.pop()
    else:
        print("Yeni kurpi kartlar = ", kurpiyeKartları)


if playerTotal.toplam() < 21:
    while True:
        istek = input("Kart Çekmek istiyor musunuz? E / H ")
        if istek == "E" or istek == "e":
            print("Yeni kartların ", playerTotal.kartCek())
            if playerTotal.toplam() >= 21:
                print(f"Kart çektin {playerTotal.toplam()} , kurpiyenin {dealeTotal.toplam()} sayısını geçemedin. KAYBETTİN")
            else:
                print(f"Sayınız {playerTotal.toplam()} kurpiyenin {dealeTotal.toplam()} sayısını geçti. KAZANDIN")
        else:
            if dealeTotal.toplam() > playerTotal.toplam():
                print(f"Kazanan KASA. {dealeTotal.toplam()} > {playerTotal.toplam()}")
            else:
                print(f"Kazanan SENSİN. {playerTotal.toplam()} > {dealeTotal.toplam()}  ")    
            break        


# print("Oyuncu toplam ",playerTotal.toplam())
# print("Kurpiye toplam ",dealeTotal.toplam())
