#!/usr/bin/env python3
# Contoh kode untuk mem-brute force 2 karakter yang hilang dari password sha1 jika kita memiliki hash-nya

import string, hashlib
from random import choice

sha1_hash = "9b4e459030ec311476e5835a450ec9cd18f50fd4"
sha1_text = "ha{}kmePHB13{}7"

# membuat list string
piece = list(string.printable)

# fungsi sha1
def _sha1(data):
    sha1_pass = hashlib.sha1(data.encode()).hexdigest()
    return sha1_pass    

# looping percobaan
while True:
    text_piece = sha1_text.format(choice(piece), choice(piece))
    print(text_piece, " => ", _sha1(text_piece))
    if _sha1(text_piece) == sha1_hash:
        print("Ketemu Passwordnya")
        print("Passwordnya: ", text_piece)
        exit(0)