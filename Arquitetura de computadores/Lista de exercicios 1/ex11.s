.data

.text

	
	main:
		
		li $t0, 0
		li $t1, 10
		li $t2, 0

	
	while:
		
		slt $s0, $t0, $t1
		beq $s0, $zero, sair

		addi $t0, $t0, 1
		addi $t2, $t2, 10
		
		j while
		


	sair:
		
		li $v0, 1
		move $a0, $t0
		syscall

		li $v0, 1
		move $a0, $t2
		syscall

		li $v0, 10
		syscall			