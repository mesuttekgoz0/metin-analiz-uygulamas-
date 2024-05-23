import tkinter as tk
from tkinter import ttk

pencere = tk.Tk()
pencere.title("Python Pencere")
pencere.geometry("700x400")

sekme_kontrol = ttk.Notebook(pencere)

sekme1 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme1, text="Sekme 1")

sekme2 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme2, text="Sekme 2")

sekme3 = ttk.Frame(sekme_kontrol)
sekme_kontrol.add(sekme3, text="Sekme 3")

sekme_kontrol.pack(expand=1, fill="both")

pencere.mainloop()


