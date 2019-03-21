#!/usr/bin/python

import os
import sys
import time
from Crypto.Cipher import AES
import string
import random

#membuat fungsi spasi banyak
def spab(xxx):
 for ccc in range(xxx):
  print(" ")

#membuat list angka dan string
#kata = list(string.ascii_lowercase)
#angka = list(range(26))
kata = list(string.ascii_lowercase)
kattaa = list(string.ascii_uppercase)
angka = list(range(10))
a26 = list(range(26))
symb = ["""/""", """@""", """!""", """#""", """$""", """%""", """*""", """(""", """)""", """'""", '''"''', """:""", """;""", """?""", """.""", """,""", """>""", """<""", """[""", """]""", """{""", """}""", """+""", """=""", """-""", """_""", """|""", """^"""] 
#membuat dictionary kata dan angka
mldi = 0
dicti = {}
dictii = {}
dictiii = {} #support huruf besar
dictiiii = {} #support simbol

for lala in range(26):
 dicti[kata[mldi]] = mldi + 400
 dictiii[kattaa[mldi]] = 300 + mldi
 dictii[str(mldi)] = 200 + mldi
 dictiii[symb[mldi]] = mldi + 500
# dictii[str(mldi)] = [kata[mldi]]
 mldi += 1
spasi = " "
kata.append(spasi)
dicti[spasi] = 99

print(dicti)
spab(10)
print(dictii)
spab(5)

#minta enkripsi dan password. LANGSUNG JADI LIST

print("""cara dekripsi:

andaikan anda punya pesan terenkripsi sebagai berikut:
                          [10, 33, 41, 26, 38]
                            /\ /\
                        ____|| ||______
10 adalah simbol pertama____|| ||______ 33 adalah simbol kedua

maka anda hanya perlu ketik simbol-simbol dan terpisahkan oleh spasi pada setiap simbolnya.
jika begini maka anda perlu mengetiknya seperti

10 33 41 26 32 b


atau langsung saja copy paste langsung seperti:
[10, 33, 41, 26, 38]                             


mudah bukan?
""")
spab(3)
print(""" ketik pesan terenkripsi.""")
pesan = input()
spab(5)
print("""ketik passwordnya.""")
password = input()

#---------------------------------------------------
#menjadikan pesan dan password --> list yang akurat
#pessan = list(pesan)
#passworrd = list(password)
#agg1 = len(pessan)
#agg2 = len(passworrd)
pesann = []
null = 0
print(pesan)
print(pesan[0])
#print(pessan)
#menggunakan  metode sekaligus.yang sama listnya, dan yang terpisahkan oleh spasi
#yang terenkripsi lagi jadi list


print(pesann)
