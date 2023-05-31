.data

.text

	main:
		
		li $t0, 15
		li $t1, 30
		
		add $t3, $t0,$t1

		

		li $v0, 1
		move $a0, $v0
		syscall	
		#chamada de sistema para imprimir o resultado		

		li $v0, 10
		syscall	
		#chamada de sistema para fechar o programa