def noktalama_temizle(metin):
    noktalama_isaretleri = "!()-[]{};:'\"\\,<>./?@#$%^&*_~="
    temiz_metin = ""
    for ch in metin:
        if ch not in noktalama_isaretleri:
            temiz_metin += ch
    return temiz_metin

def kelimesayac(metin):
    wordlist = set(metin.lower().split())
    return wordlist

def karsilastirma(metin1,metin2):
    list1 = kelimesayac(metin1)
    list2 = kelimesayac(metin2)

    samewords = list1.intersection(list2)
    allwords = list1.union(list2)

    return len(samewords) / len(allwords)

def main():

    metina = " "
    with open("metin.txt","r") as f:
        for line in f:
            metina += line

    #metina = input("Metin giriniz:")
    metinb = input("Metin giriniz:")

    print(karsilastirma(metina,metinb))

main()