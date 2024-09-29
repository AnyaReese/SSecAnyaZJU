
sbof2:	file format elf64-x86-64

Disassembly of section .init:

0000000000401000 <_init>:
  401000: f3 0f 1e fa                  	endbr64
  401004: 48 83 ec 08                  	subq	$0x8, %rsp
  401008: 48 8b 05 e9 2f 00 00         	movq	0x2fe9(%rip), %rax      # 0x403ff8 <setvbuf@GLIBC_2.2.5+0x403ff8>
  40100f: 48 85 c0                     	testq	%rax, %rax
  401012: 74 02                        	je	0x401016 <_init+0x16>
  401014: ff d0                        	callq	*%rax
  401016: 48 83 c4 08                  	addq	$0x8, %rsp
  40101a: c3                           	retq

Disassembly of section .plt:

0000000000401020 <.plt>:
  401020: ff 35 e2 2f 00 00            	pushq	0x2fe2(%rip)            # 0x404008 <_GLOBAL_OFFSET_TABLE_+0x8>
  401026: f2 ff 25 e3 2f 00 00         	repne		jmpq	*0x2fe3(%rip)   # 0x404010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40102d: 0f 1f 00                     	nopl	(%rax)
  401030: f3 0f 1e fa                  	endbr64
  401034: 68 00 00 00 00               	pushq	$0x0
  401039: f2 e9 e1 ff ff ff            	repne		jmp	0x401020 <.plt>
  40103f: 90                           	nop
  401040: f3 0f 1e fa                  	endbr64
  401044: 68 01 00 00 00               	pushq	$0x1
  401049: f2 e9 d1 ff ff ff            	repne		jmp	0x401020 <.plt>
  40104f: 90                           	nop
  401050: f3 0f 1e fa                  	endbr64
  401054: 68 02 00 00 00               	pushq	$0x2
  401059: f2 e9 c1 ff ff ff            	repne		jmp	0x401020 <.plt>
  40105f: 90                           	nop
  401060: f3 0f 1e fa                  	endbr64
  401064: 68 03 00 00 00               	pushq	$0x3
  401069: f2 e9 b1 ff ff ff            	repne		jmp	0x401020 <.plt>
  40106f: 90                           	nop

Disassembly of section .plt.sec:

0000000000401070 <.plt.sec>:
  401070: f3 0f 1e fa                  	endbr64
  401074: f2 ff 25 9d 2f 00 00         	repne		jmpq	*0x2f9d(%rip)   # 0x404018 <_GLOBAL_OFFSET_TABLE_+0x18>
  40107b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
  401080: f3 0f 1e fa                  	endbr64
  401084: f2 ff 25 95 2f 00 00         	repne		jmpq	*0x2f95(%rip)   # 0x404020 <_GLOBAL_OFFSET_TABLE_+0x20>
  40108b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
  401090: f3 0f 1e fa                  	endbr64
  401094: f2 ff 25 8d 2f 00 00         	repne		jmpq	*0x2f8d(%rip)   # 0x404028 <_GLOBAL_OFFSET_TABLE_+0x28>
  40109b: 0f 1f 44 00 00               	nopl	(%rax,%rax)
  4010a0: f3 0f 1e fa                  	endbr64
  4010a4: f2 ff 25 85 2f 00 00         	repne		jmpq	*0x2f85(%rip)   # 0x404030 <_GLOBAL_OFFSET_TABLE_+0x30>
  4010ab: 0f 1f 44 00 00               	nopl	(%rax,%rax)

Disassembly of section .text:

00000000004010b0 <_start>:
  4010b0: f3 0f 1e fa                  	endbr64
  4010b4: 31 ed                        	xorl	%ebp, %ebp
  4010b6: 49 89 d1                     	movq	%rdx, %r9
  4010b9: 5e                           	popq	%rsi
  4010ba: 48 89 e2                     	movq	%rsp, %rdx
  4010bd: 48 83 e4 f0                  	andq	$-0x10, %rsp
  4010c1: 50                           	pushq	%rax
  4010c2: 54                           	pushq	%rsp
  4010c3: 45 31 c0                     	xorl	%r8d, %r8d
  4010c6: 31 c9                        	xorl	%ecx, %ecx
  4010c8: 48 c7 c7 05 12 40 00         	movq	$0x401205, %rdi         # imm = 0x401205
  4010cf: ff 15 1b 2f 00 00            	callq	*0x2f1b(%rip)           # 0x403ff0 <setvbuf@GLIBC_2.2.5+0x403ff0>
  4010d5: f4                           	hlt
  4010d6: 66 2e 0f 1f 84 00 00 00 00 00	nopw	%cs:(%rax,%rax)

00000000004010e0 <_dl_relocate_static_pie>:
  4010e0: f3 0f 1e fa                  	endbr64
  4010e4: c3                           	retq
  4010e5: 66 2e 0f 1f 84 00 00 00 00 00	nopw	%cs:(%rax,%rax)
  4010ef: 90                           	nop

00000000004010f0 <deregister_tm_clones>:
  4010f0: b8 48 40 40 00               	movl	$0x404048, %eax         # imm = 0x404048
  4010f5: 48 3d 48 40 40 00            	cmpq	$0x404048, %rax         # imm = 0x404048
  4010fb: 74 13                        	je	0x401110 <deregister_tm_clones+0x20>
  4010fd: b8 00 00 00 00               	movl	$0x0, %eax
  401102: 48 85 c0                     	testq	%rax, %rax
  401105: 74 09                        	je	0x401110 <deregister_tm_clones+0x20>
  401107: bf 48 40 40 00               	movl	$0x404048, %edi         # imm = 0x404048
  40110c: ff e0                        	jmpq	*%rax
  40110e: 66 90                        	nop
  401110: c3                           	retq
  401111: 66 66 2e 0f 1f 84 00 00 00 00 00     	nopw	%cs:(%rax,%rax)
  40111c: 0f 1f 40 00                  	nopl	(%rax)

0000000000401120 <register_tm_clones>:
  401120: be 48 40 40 00               	movl	$0x404048, %esi         # imm = 0x404048
  401125: 48 81 ee 48 40 40 00         	subq	$0x404048, %rsi         # imm = 0x404048
  40112c: 48 89 f0                     	movq	%rsi, %rax
  40112f: 48 c1 ee 3f                  	shrq	$0x3f, %rsi
  401133: 48 c1 f8 03                  	sarq	$0x3, %rax
  401137: 48 01 c6                     	addq	%rax, %rsi
  40113a: 48 d1 fe                     	sarq	%rsi
  40113d: 74 11                        	je	0x401150 <register_tm_clones+0x30>
  40113f: b8 00 00 00 00               	movl	$0x0, %eax
  401144: 48 85 c0                     	testq	%rax, %rax
  401147: 74 07                        	je	0x401150 <register_tm_clones+0x30>
  401149: bf 48 40 40 00               	movl	$0x404048, %edi         # imm = 0x404048
  40114e: ff e0                        	jmpq	*%rax
  401150: c3                           	retq
  401151: 66 66 2e 0f 1f 84 00 00 00 00 00     	nopw	%cs:(%rax,%rax)
  40115c: 0f 1f 40 00                  	nopl	(%rax)

0000000000401160 <__do_global_dtors_aux>:
  401160: f3 0f 1e fa                  	endbr64
  401164: 80 3d 1d 2f 00 00 00         	cmpb	$0x0, 0x2f1d(%rip)      # 0x404088 <completed.0>
  40116b: 75 13                        	jne	0x401180 <__do_global_dtors_aux+0x20>
  40116d: 55                           	pushq	%rbp
  40116e: 48 89 e5                     	movq	%rsp, %rbp
  401171: e8 7a ff ff ff               	callq	0x4010f0 <deregister_tm_clones>
  401176: c6 05 0b 2f 00 00 01         	movb	$0x1, 0x2f0b(%rip)      # 0x404088 <completed.0>
  40117d: 5d                           	popq	%rbp
  40117e: c3                           	retq
  40117f: 90                           	nop
  401180: c3                           	retq
  401181: 66 66 2e 0f 1f 84 00 00 00 00 00     	nopw	%cs:(%rax,%rax)
  40118c: 0f 1f 40 00                  	nopl	(%rax)

0000000000401190 <frame_dummy>:
  401190: f3 0f 1e fa                  	endbr64
  401194: eb 8a                        	jmp	0x401120 <register_tm_clones>

0000000000401196 <prepare>:
  401196: f3 0f 1e fa                  	endbr64
  40119a: 55                           	pushq	%rbp
  40119b: 48 89 e5                     	movq	%rsp, %rbp
  40119e: 48 8b 05 cb 2e 00 00         	movq	0x2ecb(%rip), %rax      # 0x404070 <stdin@GLIBC_2.2.5>
  4011a5: b9 00 00 00 00               	movl	$0x0, %ecx
  4011aa: ba 02 00 00 00               	movl	$0x2, %edx
  4011af: be 00 00 00 00               	movl	$0x0, %esi
  4011b4: 48 89 c7                     	movq	%rax, %rdi
  4011b7: e8 e4 fe ff ff               	callq	0x4010a0 <.plt.sec+0x30>
  4011bc: 48 8b 05 9d 2e 00 00         	movq	0x2e9d(%rip), %rax      # 0x404060 <stdout@GLIBC_2.2.5>
  4011c3: b9 00 00 00 00               	movl	$0x0, %ecx
  4011c8: ba 02 00 00 00               	movl	$0x2, %edx
  4011cd: be 00 00 00 00               	movl	$0x0, %esi
  4011d2: 48 89 c7                     	movq	%rax, %rdi
  4011d5: e8 c6 fe ff ff               	callq	0x4010a0 <.plt.sec+0x30>
  4011da: 48 8b 05 9f 2e 00 00         	movq	0x2e9f(%rip), %rax      # 0x404080 <stderr@GLIBC_2.2.5>
  4011e1: b9 00 00 00 00               	movl	$0x0, %ecx
  4011e6: ba 02 00 00 00               	movl	$0x2, %edx
  4011eb: be 00 00 00 00               	movl	$0x0, %esi
  4011f0: 48 89 c7                     	movq	%rax, %rdi
  4011f3: e8 a8 fe ff ff               	callq	0x4010a0 <.plt.sec+0x30>
  4011f8: bf 1e 00 00 00               	movl	$0x1e, %edi
  4011fd: e8 7e fe ff ff               	callq	0x401080 <.plt.sec+0x10>
  401202: 90                           	nop
  401203: 5d                           	popq	%rbp
  401204: c3                           	retq

0000000000401205 <main>:
  401205: f3 0f 1e fa                  	endbr64
  401209: 55                           	pushq	%rbp
  40120a: 48 89 e5                     	movq	%rsp, %rbp
  40120d: 48 81 ec 10 01 00 00         	subq	$0x110, %rsp            # imm = 0x110
  401214: 89 bd fc fe ff ff            	movl	%edi, -0x104(%rbp)
  40121a: 48 89 b5 f0 fe ff ff         	movq	%rsi, -0x110(%rbp)
  401221: b8 00 00 00 00               	movl	$0x0, %eax
  401226: e8 6b ff ff ff               	callq	0x401196 <prepare>
  40122b: 48 8d 85 00 ff ff ff         	leaq	-0x100(%rbp), %rax
  401232: 48 89 c6                     	movq	%rax, %rsi
  401235: bf 04 20 40 00               	movl	$0x402004, %edi         # imm = 0x402004
  40123a: b8 00 00 00 00               	movl	$0x0, %eax
  40123f: e8 2c fe ff ff               	callq	0x401070 <.plt.sec>
  401244: 48 8d 85 00 ff ff ff         	leaq	-0x100(%rbp), %rax
  40124b: 48 89 c7                     	movq	%rax, %rdi
  40124e: b8 00 00 00 00               	movl	$0x0, %eax
  401253: e8 38 fe ff ff               	callq	0x401090 <.plt.sec+0x20>
  401258: b8 00 00 00 00               	movl	$0x0, %eax
  40125d: c9                           	leave
  40125e: c3                           	retq

Disassembly of section .fini:

0000000000401260 <_fini>:
  401260: f3 0f 1e fa                  	endbr64
  401264: 48 83 ec 08                  	subq	$0x8, %rsp
  401268: 48 83 c4 08                  	addq	$0x8, %rsp
  40126c: c3                           	retq
