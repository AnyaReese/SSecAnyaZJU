TARGETS := interact1.elf interact2.elf interact4.elf interact5.elf interact6.elf

all: $(TARGETS)

%.elf: %.c
	gcc $^ -o $@

clean:
	rm -f $(TARGETS)