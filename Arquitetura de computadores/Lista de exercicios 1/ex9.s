.data

.text

	
	main: 

		li $t0, 7
		li $t1, 5
		li $t2, 20
		
		move $t2, $t0
		# move o valor de t0 para t2

		slt $s0, $t1, $t2
		
		beq $s0, $zero, sair 

		move $t1, $t2

		li $v0, 1
		move $a0, $t1
		syscall

		li $v0, 10
		syscall
		


	sair: 
		
		li $v0, 10
		syscall
		
