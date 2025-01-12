Program is compiled like:
- gcc program.c -o program -Wl,-z,relro -no-pie -L. -ltiny

Can run program with:
- LD_LIBRARY_PATH=. ./program

