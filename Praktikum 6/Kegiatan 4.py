Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Flanika Vidya Faresty'
>>> NIM = 185
>>> Tinggi = 160
>>> Berat = 50
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Aku merupakan tipe data tuple karena ditulis dengan kurung
>>> Aku[0]
2001
>>> # Karena 'TahunLahir' berada di paling awal pada data aku
>>> a = NIM % 4 ; Aku[a]
50
>>> # Karena 185 % 4 menghasilkan 1,Maka menunjuk pada berat badan
>>> type(Aku[4])
<class 'str'>
>>> # Karena berisi tulisan dan diawali dengan tanda petik
>>> Aku[a:4]
(50, 160, 185)
>>> # Karena menunjuk bagian dari satu sampai sebelum 4
>>> type(Aku[4])
<class 'str'>
>>> # Karena berisi tulisan dan diawali dengan tanda petik
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Error karena elemen tuple tidak bisa dirubah
>>> type(Data)
<class 'list'>
>>> # Data merupakan tipe data list karena ditulis denngan kurung siku
>>> type(Data[4])
<class 'str'>
>>> # Karena berisi tulisan dan diawali tanda petik
>>> Data[4][5]
'k'
>>> # Menunjuk data ke-5(diawali dari 0)dari 'Nama'
>>> Data[4][a:6]
'lanik'
>>> # Menunjuk data ke-2 sampai sebelum 6 dari 'Nama'
>>> Data[0] = 'ok'; Data
['ok', 50, 160, 185, 'Flanika Vidya Faresty']
>>> # Karena elemen list dapat diubah
>>> Data[-a]
'Flanika Vidya Faresty'
>>> # Karena memanggil element paling akhir
>>> range(a)
range(0, 1)
>>> # Karena menunjuk dari 0 sampai 'a'
