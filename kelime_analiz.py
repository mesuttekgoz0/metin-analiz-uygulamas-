def gereksiz_karakter_temizle(metin):
    noktalama_isaretleri = "!()-[]{};:'\"\\,<>./?@#$%^&*_~="
    gereksiz_kelimeler = "ile","ve","veya","ya da","hem","de","da"
    temiz_metin = ""
    for ch in metin:
        if ch not in noktalama_isaretleri and ch not in gereksiz_kelimeler:
            temiz_metin += ch
    return temiz_metin

def wordlist(metin):
    wordlist = set(metin.lower().split())
    return wordlist

def karsilastirma(metin1,metin2):
    list1 = wordlist(metin1)
    list2 = wordlist(metin2)

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