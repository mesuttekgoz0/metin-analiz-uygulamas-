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
        kelime = kelime.strip(string.punctuation) # Noktalama işaretlerini siler
        if kelime.lower() not in gereksiz_kelimeler:
            temiz_metin += kelime + " "
    text.delete("1.0", tk.END)
    text.insert(tk.END, temiz_metin)

pencere = tk.Tk()
pencere.title("Python Pencere")
pencere.geometry("400x300")

sekme_kontrol = ttk.Notebook(pencere)

sekme1 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme1, text="Sekme 1")

text = tk.Text(sekme1,width=70,height=10)
text.pack(fill=tk.BOTH, expand=1)

doysa_yükle_butonu=tk.Button(sekme1,text="dosya yükle")
doysa_yükle_butonu.pack()
doysa_yükle_butonu.bind("<Button-1>", dosya_sec)

temizle_buton = tk.Button(sekme1, text="Temizle", command=temizle)
temizle_buton.pack()


sekme2 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme2, text="Sekme 2")

text1 = tk.Text(sekme2,width=30,height=2)
text1.pack(fill=tk.BOTH, expand=0, pady=10)

text2 = tk.Text(sekme2,width=70,height=2)
text2.pack(fill=tk.BOTH, expand=0, pady=30)


sekme3 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme3, text="Sekme 3")

sekme_kontrol.pack(expand=1, fill="both")

gereksiz_kelimeler = ["ve", "veya", "ama", "ise", "ile"] # Gereksiz kelimeler listesi

pencere.mainloop()