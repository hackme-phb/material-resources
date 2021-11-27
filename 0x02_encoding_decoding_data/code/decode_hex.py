#!/usr/bin/env python3

import binascii

enc = "68 34 63 6B 6D 33 7B 68 65 78 34 5F 64 65 63 69 6D 61 6C 7D"
replace = enc.replace(" ", "")
print(binascii.unhexlify(replace).decode())