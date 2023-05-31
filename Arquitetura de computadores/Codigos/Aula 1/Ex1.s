.data

.text

main:
    addi $t0, $zero, 15
    addi $t1, $zero, 30
    add $t3, $t1, $t0
    #adicao de t1 com t0 em t3
    
    li $v0, 1
    add  $a0, $zero, $t3
    syscall
    #chamada para imprimir o resultado
    
    li $v0, 10
    syscall
    #chamada para fechar o sistema