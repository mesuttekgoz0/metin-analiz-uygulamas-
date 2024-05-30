import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import string
import Levenshtein
import collections


def dosya_sec(event):
    dosya_yolu = filedialog.askopenfilename()
    if dosya_yolu:
        with open(dosya_yolu, 'r') as dosya:
            icerik = dosya.read()
            text.insert(tk.END, icerik)


def temizle():
    metin = text.get("1.0", tk.END)
    temiz_metin = ""
    for kelime in metin.split():
        kelime = kelime.strip(string.punctuation)  # Noktalama işaretlerini siler
        if kelime.lower() not in gereksiz_kelimeler:
            temiz_metin += kelime + " "
    text.delete("1.0", tk.END)
    text.insert(tk.END, temiz_metin)


def benzerlik_analizi():
    metin1_icerik = text1.get("1.0", tk.END)
    metin2_icerik = text2.get("1.0", tk.END)

    benzerlik_orani = Levenshtein.ratio(metin1_icerik, metin2_icerik)

    yüzde = 100 * benzerlik_orani

    # Benzerlik oranını yeni bir pencerede göster
    benzerlik_penceresi = tk.Toplevel(pencere)
    benzerlik_penceresi.title("Benzerlik Analizi")
    benzerlik_penceresi.geometry("200x100")

    benzerlik_etiketi = tk.Label(benzerlik_penceresi, text=f"Benzerlik Oranı: %{yüzde:.2f}")
    benzerlik_etiketi.pack(pady=20)


def bul_ve_isaretle():
    kelime = kelime_giris.get().strip()  # Giriş kutusundaki kelimeyi alır ve başındaki ve sonundaki boşlukları kaldırır
    metin = text.get("1.0", tk.END)
    if not kelime:
        messagebox.showinfo("Bilgi", "Lütfen bir kelime girin.")
        return

    # Önce mevcut işaretlemeleri temizle
    text.tag_remove("highlight", "1.0", tk.END)

    # Kelimenin tüm geçişlerini bul ve işaretle
    kelime_bulundu = False
    baslangic = 1.0
    while True:
        baslangic = text.search(kelime, baslangic, stopindex=tk.END)
        if not baslangic:
            break
        kelime_bulundu = True
        bitis = f"{baslangic}+{len(kelime)}c"
        text.tag_add("highlight", baslangic, bitis)
        baslangic = bitis

    if not kelime_bulundu:
        messagebox.showinfo("Bilgi", "Aranan kelime metinde bulunamadı.")

    # İşaretleme stilini ayarla
    text.tag_config("highlight", background="yellow", foreground="black")

def analiz_et():
    metin = text.get("1.0", tk.END)
    kelimeler = metin.split()
    kelime_sayisi = len(kelimeler)
    kelime_sayisi_dict = collections.Counter(kelimeler)

    # En çok geçen kelimeyi bul
    en_cok_gecen_kelime = kelime_sayisi_dict.most_common(1)[0][0]
    en_cok_gecen_kelime_sayisi = kelime_sayisi_dict.most_common(1)[0][1]

    # En az geçen kelimeyi bul
    en_az_gecen_kelime = kelime_sayisi_dict.most_common()[-1][0]
    en_az_gecen_kelime_sayisi = kelime_sayisi_dict.most_common()[-1][1]

    # Harf sayısını bul
    harf_sayisi = sum(len(kelime) for kelime in kelimeler)

    # Bilgileri yeni bir pencerede göster
    bilgi_penceresi = tk.Toplevel(pencere)
    bilgi_penceresi.title("En Çok ve En Az Geçen Kelimeler")
    bilgi_penceresi.geometry("300x150")

    en_cok_gecen_k_label = tk.Label(bilgi_penceresi, text=f"En Çok Geçen Kelime: {en_cok_gecen_kelime} ({en_cok_gecen_kelime_sayisi} kez)")
    en_cok_gecen_k_label.pack(pady=10)
    en_az_gecen_k_label = tk.Label(bilgi_penceresi, text=f"En Az Geçen Kelime: {en_az_gecen_kelime} ({en_az_gecen_kelime_sayisi} kez)")
    en_az_gecen_k_label.pack()
    kelime_sayisi_label = tk.Label(bilgi_penceresi, text=f"Toplam Kelime Sayısı: {kelime_sayisi}")
    kelime_sayisi_label.pack(pady=10)
    harf_sayisi_label = tk.Label(bilgi_penceresi, text=f"Toplam Harf Sayısı: {harf_sayisi}")
    harf_sayisi_label.pack()


pencere = tk.Tk()
pencere.title("analiz uyguılaması")
pencere.geometry("400x500")
pencere.configure(bg="#242424")

sekme_kontrol = ttk.Notebook(pencere)

sekme1 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme1, text="text işlem")


text = tk.Text(sekme1, width=70, height=10)
text.pack(fill=tk.BOTH, expand=1)

doysa_yükle_butonu = tk.Button(sekme1, text="dosya yükle")
doysa_yükle_butonu.pack()
doysa_yükle_butonu.bind("<Button-1>", dosya_sec)

temizle_buton = tk.Button(sekme1, text="Temizle", command=temizle)
temizle_buton.pack()

kelime_giris = tk.Entry(sekme1)
kelime_giris.pack()

bul_isaretley_butonu = tk.Button(sekme1, text="Kelime Bul ve İşaretle", command=bul_ve_isaretle,bg="light green")
bul_isaretley_butonu.pack()

text_analiz_buton= tk.Button(sekme1, text="analiz sonuçları",bg="light green",command=analiz_et)
text_analiz_buton.pack()

sekme2 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme2, text="benzerlik analizi")

text1 = tk.Text(sekme2, width=30, height=2)
text1.pack(fill=tk.BOTH, expand=0, pady=10)

text2 = tk.Text(sekme2, width=70, height=2)
text2.pack(fill=tk.BOTH, expand=0, pady=30)

analiz_butonu = tk.Button(sekme2, text="Benzerliği Analiz Et", command=benzerlik_analizi)
analiz_butonu.pack()

sekme_kontrol.pack(expand=1, fill="both")

gereksiz_kelimeler = ["ve", "veya", "ama", "ise", "ile","birkaç","hem","ile","de","da","ya da"]  # Gereksiz kelimeler listesi

pencere.mainloop()

