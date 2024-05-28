import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import string
import Levenshtein


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
    temiz_metin = metin

    if kelime:
        kelime_baslangic = metin.find(kelime)
        if kelime_baslangic != -1:
            kelime_bitis = kelime_baslangic + len(kelime)
            temiz_metin = temiz_metin[:kelime_baslangic] + f"[{kelime}]" + temiz_metin[kelime_bitis:]
        else:
            # Eğer kelime bulunamazsa bir uyarı mesajı göster
            tk.messagebox.showinfo("Bilgi", "Aranan kelime metinde bulunamadı.")

    text.delete("1.0", tk.END)
    text.insert(tk.END, temiz_metin)


pencere = tk.Tk()
pencere.title("Python Pencere")
pencere.geometry("400x300")

sekme_kontrol = ttk.Notebook(pencere)

sekme1 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme1, text="Sekme 1")

text = tk.Text(sekme1, width=70, height=10)
text.pack(fill=tk.BOTH, expand=1)

doysa_yükle_butonu = tk.Button(sekme1, text="dosya yükle")
doysa_yükle_butonu.pack()
doysa_yükle_butonu.bind("<Button-1>", dosya_sec)

temizle_buton = tk.Button(sekme1, text="Temizle", command=temizle)
temizle_buton.pack()

kelime_giris = tk.Entry(sekme1)
kelime_giris.pack()

bul_isaretley_butonu = tk.Button(sekme1, text="Kelime Bul ve İşaretle", command=bul_ve_isaretle)
bul_isaretley_butonu.pack()

sekme2 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme2, text="Sekme 2")

text1 = tk.Text(sekme2, width=30, height=2)
text1.pack(fill=tk.BOTH, expand=0, pady=10)

text2 = tk.Text(sekme2, width=70, height=2)
text2.pack(fill=tk.BOTH, expand=0, pady=30)

analiz_butonu = tk.Button(sekme2, text="Benzerliği Analiz Et", command=benzerlik_analizi)
analiz_butonu.pack()

sekme_kontrol.pack(expand=1, fill="both")

gereksiz_kelimeler = ["ve", "veya", "ama", "ise", "ile"]  # Gereksiz kelimeler listesi

pencere.mainloop()

