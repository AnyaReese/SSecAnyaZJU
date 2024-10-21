all: demo fsb1 fsb2 bonus

demo:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector demo.c

fsb1:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector fsb1.c

fsb2:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector fsb2.c

bonus:
	gcc -o $@ -fno-pie -no-pie -fno-stack-protector bonus.c


clean:
	rm demo fsb1 fsb2 bonus

