from pwn import *

p = process("./interact4.elf") # launch target ELF program
                               # with input/output wrapper

print(p.recv()) # print what the program output
p.sendline(b"\xaa\xbb\xcc\xdd\xee\xff\n") # input this bytes to program

p.interactive() # enter into shell-like interaction