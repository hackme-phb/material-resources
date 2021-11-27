#!/usr/bin/env python3
# Contoh kode untuk mem-brute force 2 karakter yang hilang dari password md5 jika kita memiliki hash-nya

import string, hashlib
from random import choice

md5_hash = "8f9b093a619b867adf311b02fbfc1fd1"
md5_text = "hac{}mePHB1{}12"

# membuat list string
piece = list(string.printable)

# fungsi md5
def _md5(data):
    md5_pass = hashlib.md5(data.encode()).hexdigest()
    return md5_pass

# looping percobaan
while True:
    text_piece = md5_text.format(choice(piece), choice(piece))
    print(text_piece, " => ", _md5(text_piece))
    if _md5(text_piece) == md5_hash:
        print("Ketemu Passwordnya")
        print("Passwordnya: ", text_piece)
        exit(0)