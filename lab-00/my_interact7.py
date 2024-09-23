from pwn import *

p = process("./interact5.elf") # launch target ELF program
                               # with input/output wrapper


buffer = p.recv(8)
print(buffer) # print what the program output

payload = p64(u64(buffer) ^ 0xaaaaaaaaaaaaaaaa)
payload += b"\n"
p.sendlineafter("Enter your password:", payload)

p.interactive() # enter into shell-like interaction