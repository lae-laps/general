# x86 syntax for linux kernel system call to exit with status  0

.section .data
.section .text
.globl __start
__start:

movl $1 %eax
movl $0 %ebx

int $0x80
