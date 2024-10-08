all: rop1 rop2 rop3

rop1:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector rop1.c

rop2:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector -static rop2.c

rop3:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector rop3.c

clean:
	rm rop1 rop2 rop3