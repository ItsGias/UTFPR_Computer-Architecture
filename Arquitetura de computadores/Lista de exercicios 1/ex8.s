.data

.text

	main:	
		
		li $v0,5
		syscall
		move $t0,$v0
		
		li $v0,5
		syscall
		move $t1,$v0
		
	
	multiplicar:
			
			beq $t1, $zero, sair
			addi $t1, $t1, -1
			add $s0, $s0, $t0
			j multiplicar
				
	sair:	
	
			li $v0,1
			move $a0, $s0
			syscall
			
			li $v0,10
			syscall
