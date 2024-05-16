def harf(örnek):

    harf_sayısı = 0

    for karakter in örnek:

        if karakter.isalpha():
            harf_sayısı += 1

    print("Toplam harf sayısı:", harf_sayısı)

def kelime_sayısı(örnek):


    kelimeler = örnek.split()
    kelime=len(kelimeler)

    print(f"Toplam kelime sayısı: {kelime}")



örnek="ssf thtg"
harf(örnek)
kelime_sayısı(örnek)
