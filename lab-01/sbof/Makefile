all: sbof1 sbof2

sbof1:
	gcc -o $@ -z execstack -fno-pie -no-pie -fno-stack-protector sbof1.c

sbof2:
	gcc -o $@ -z execstack -fno-pie -no-pie -fno-stack-protector sbof2.c

clean:
	rm sbof1 sbof2