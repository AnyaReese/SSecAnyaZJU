from pwn import *
from typing import Tuple
import re

context.log_level = 'DEBUG'

context.binary = elf = ELF("./example")

p = process(elf.path)

def handle_add(name: bytes, password: bytes, intro: bytes, motto: bytes) -> int:
    p.recvuntil(b"[ 5 ] leave\n> ")
    p.sendline(b"1")
    p.recvuntil(b"name > ")
    p.sendline(name)
    p.recvuntil(b"password > ")
    p.sendline(password)
    p.recvuntil(b"introduction > ")
    p.sendline(intro)
    p.recvuntil(b"motto > ")
    p.sendline(motto)
    p.recvuntil(b"at index ", drop=True)
    data = p.recvline().strip()
    return int(data)

def handle_del(index: int, password: bytes) -> None:
    p.recvuntil(b"[ 5 ] leave\n> ")
    p.sendline(b"2")
    p.recvuntil(b"index > ")
    p.sendline(str(index))
    p.recvuntil(b"password > ")
    p.sendline(password)
    return

def handle_show(index: int, password: bytes) -> Tuple[bytes, bytes, bytes]:
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

def handle_edit(
    index: int, password: bytes, edit_name: bytes, edit_intro: bytes, edit_motto: bytes
):
    p.recvuntil(b"[ 5 ] leave\n> ")
    p.sendline(b"4")
    p.recvuntil(b"index > ")
    p.sendline(str(index))
    p.recvuntil(b"password > ")
    p.sendline(password)

    p.recvuntil(b"new name > ")
    p.sendline(edit_name)
    p.recvuntil(b"new introduction > ")
    p.sendline(edit_intro)
    p.recvuntil(b"new motto > ")
    p.sendline(edit_motto)
    return


bob_idx = handle_add(b"Bob", b"123456", b"hello there, i am bob", b"try everything")
alice_idx = handle_add(b"Alice", b"654321", b"hi everyone, i am alice", b"eat more vegetables")
jimmy_idx = handle_add(b"Jimmy", b"abc321", b"didotidido", b"<blank/>")
jack_idx = handle_add(b"Jack", b"p4ssw0rd", b"blablabla", b"...")
charles_idx = handle_add(b"Charles", b"aaabbb", b"Beautiful is better than ugly", b"<alert>")
mark_idx = handle_add(b"Mark", b"marknb11", b"Explicit is better than implicit", b"watch out")
vincent_idx = handle_add(b"Vincent", b"m950524", b"my name is vincent! vincent", b"________")
william_idx = handle_add(b"William", b"will32123", b'dG9vb29vb29vb29oYW5kc29tZQ==', b"i'm fine")
joseph_idx = handle_add(b"Joseph", b"jjj789", b'XD', b"Teach me and I remember.")
henry_idx = handle_add(b"Herry", b"hABC321", b'no intro at all', b"hard-working!")
gary_idx = handle_add(b"Gary", b"ggwp2024", b'the best gary in the world', b"I never walk backwards.")

handle_del(vincent_idx, b"m950524")
handle_del(mark_idx, b"marknb11")
handle_del(charles_idx, b"aaabbb")
handle_del(jack_idx, b"p4ssw0rd")
handle_del(jimmy_idx, b"abc321")
handle_del(alice_idx, b"654321")
handle_del(bob_idx, b"123456")
# handle_del(william_idx, b"will32123")
# handle_del(joseph_idx, b"jjj789")

p.recvuntil(b"[ 5 ] leave\n> ")
p.sendline(b"6")
p.recvuntil(b"[ 5 ] leave\n> ")
p.sendline(b"5")
p.close()