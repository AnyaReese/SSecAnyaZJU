build:
	# docker pull gcc:7.5.0
	docker run --rm -v ${PWD}:/usr/src/myapp -w /usr/src/myapp gcc:7.5.0 gcc -o example ./example.c
	sudo chmod 777 example
	patchelf --set-interpreter ./ld-2.31.so ./example
	patchelf --replace-needed libc.so.6 ./libc-2.31.so ./example

clean:
	rm -f example
