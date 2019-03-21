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
huruf = list(string.ascii_lowercase)
angka = list(range(26))
 
#membuat dictionary kata dan angka
dicti = {}
dictii = {}
spasi = {' ': ' '}
nol = 0
for vvv in range(26):
 dicti[huruf[nol]] = nol
 dictii[angka[nol]] = huruf[nol]
 nol += 1

print(dicti)
spab(10)
print(dictii)
spab(5)

#minta enkripsi dan password. LANGSUNG JADI LIST

print("""cara dekripsi:

andaikan anda punya pesan terenkripsi sebagai berikut:
                          [10, 33, 41, 26, 32, ['b']]
                            /\ /\
                        ____|| ||______
10 adalah simbol pertama____|| ||______ 33 adalah simbol kedua                             

maka anda hanya perlu ketik simbol-simbol dan terpisahkan oleh spasi pada setiap simbolnya.
jika begini maka anda perlu mengetiknya seperti

10 33 41 26 32 b

mudah bukan?
""")
spab(3)
print(""" ketik pesan terenkripsi.""")
pesan = input()
spab(5)
print("""ketik passwordnya."""")
password = input()

#---------------------------------------------------
#menjadikan pesan dan password --> list yang akurat
pessan = list(pesan)
passworrd = list(password)
agg1 = len(pessan)
agg2 = len(passworrd)
pesann = []

