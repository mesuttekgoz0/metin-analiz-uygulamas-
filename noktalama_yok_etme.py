def noktalama_temizle(metin):
    noktalama_isaretleri = "!()-[]{};:'\"\\,<>./?@#$%^&*_~="
    temiz_metin = ""
    for ch in metin:
        if ch not in noktalama_isaretleri:
            temiz_metin += ch
    return temiz_metin

# Örnek kullanım:
metin = input("Metin giriniz:\n")
temiz_metin = noktalama_temizle(metin)
print("Temiz metin:", temiz_metin)