from tkinter import *

aplikasi = Tk()
aplikasi.title("bangunann")

L = Label(aplikasi, text="Bangun Geometri", font=('Arial Black', 20))
L.grid(row=0, column=0, sticky="W", columnspan=3)


L22 = Label(aplikasi, text="Piramid adalah piramida dengan alas persegi yang membutuhkan 2 parameter yaitu alas dan tinggi segitiga")
L22.grid(row=1, column=0, sticky="W", columnspan=10)


L2 = Label(aplikasi, text="Alas Segitiga : ")
L2.grid(row=2, column=0, sticky="W", columnspan=3)



alas = StringVar()
L5 = Entry(aplikasi, textvariable=alas)
L5.grid(row=2, column=1, sticky="W")

######----------------------------------------

L3 = Label(aplikasi, text="Tinggi Segitiga : ")
L3.grid(row=3, column=0, sticky="W", columnspan=3)



tinggi = StringVar()
L6 = Entry(aplikasi, textvariable=tinggi)
L6.grid(row=3, column=1, sticky="W")

####--------------------------------------------

def hitung():
    segitiga = (float(alas.get()) * float(tinggi.get())) * 4
    alasnya = float(alas.get()) * float(alas.get())
    hasil = segitiga + alasnya
    Lhasil.config(text=hasil)
###----------tombol-----------
b1 = Button(aplikasi, text="Hitung Luas", command=hitung)
b1.grid(row=4, column=0)


LJhasil = Label(aplikasi, text="Hasil : ")
LJhasil.grid(row=4, column=1, sticky="W", columnspan=3)


Lhasil = Label(aplikasi, text="")
Lhasil.grid(row=4, column=2, sticky="W")







aplikasi.mainloop()

