#!/usr/bin/env python3

enc = "104 52 99 107 109 51 123 116 101 120 116 95 116 111 95 100 101 99 105 109 97 108 125"
split = enc.split(" ")
print (''.join([chr(int(x)) for x in split]))