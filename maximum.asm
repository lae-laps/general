# This algorithm implemented in x86 ASM is intended to find the largest integer within a list of numbers
# Register Use:
#
# %eax - current data item
# %ebx - largest data item
# %edi - index of the data item being examined

.section .data

data_items:     # the data items we are going to examine
    .long 3, 67, 34, 222, 45, 75, 54, 34, 44, 33, 22, 11, 224, 66, 0

.section .text

.globl _start
_start:
    movl $0, %edi                       # start the count register at position 0
    movl data_items(,%edi,4), %eax      # load first byte of data
    movl %eax, %ebx                     # since it's the first item, %eax is the biggest number

start_loop:                             # start of loop
    cmpl $0, %eax                       # check if we have reached the end
    je   loop_exit
    incl %edi                           # increment %edi by one - load next item
    movl data_items(,%edi,4), %eax
    cmpl %ebx, %eax                     # compare largest value to current value
    jle  start_loop                      # jump to loop beggining if not bigger
    movl %eax, %ebx                     # move the current item as the biggest item (only happens if cmpl was successfull)
    jmp  start_loop                      # jump to the start of the loop

loop_exit:                              # on loop exit we produce a kernel interrupt to exit with the biggest number as return code
    movl $1, %eax                       # move 1 (interrupt number for exit) to %eax - biggest number already in %ebx
    int  $0x80                           # call the interrupt
