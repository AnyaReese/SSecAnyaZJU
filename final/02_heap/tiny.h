#ifndef TINYHEAP
#define TINYHEAP

#define TINYHEAP_BASE (0x10000)
void *tiny_alloc(unsigned int);
void tiny_free(void *);

#endif