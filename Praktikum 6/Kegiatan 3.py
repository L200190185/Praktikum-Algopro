Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Flanika Vidya Faresty'
>>> NIM = 'L200190185'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Karena 'x' merupakan data yang bertype integer
>>> type(b)
<class 'int'>
>>> # Karena data 'Nama' memiliki instruksi 'len'
>>> a / b
56.42857142857143
>>> # Karena hasil '1185' dibagi '21' adalah 56.42857142857143
>>> a // b
56
>>> # Karena arti '//' adalah pembagian dengan pembulatan ke bawah
>>> 10 * (a - 999)
1860
>>> # Karena nilai 'a' setelah dikurangkan 999 adalah 186 dan dikalikan 10 adalah 1860
>>> b ** 2
441
>>> # Karena makna '**' adalah pangkat
>>> a % b
9
>>> # Karena makna '%' adalah sisa hasil bagi
>>> c = 12.5
>>> type(c)
<class 'float'>
>>> # Karena '12.5' adalah angka desimal
>>> a / c
94.8
>>> # Karena hasil '1185' dibagi dengan '12.5' adalah 94.8
>>> a // c
94.0
>>> # Karena arti '//' adalah pembagian dengan pembulatan ke bawah
>>> a % c
10.0
>>> # Karena makna '%' adalah sisa hasil bagi
>>> c > b
False
>>> # Karena nominal 'c' adalah 12.5 dan nominal 'b' adalah 21, salah karena lebih besar bilangan 'b'
>>> type(c > b)
<class 'bool'>
>>> # Karena hasil dari 'bool' adalah TRUE dan FALSE
>>> a > b and b > c
True
>>> # Karena bilangan 'a' lebih besar dari 'b' dan bilangan 'b' lebih besar dari 'c'
>>> a > 1100 or b < 10
True
>>> # Karena bilangan 'a' lebih besar dari '1100' atau 'b' lebih besar dari '10'
