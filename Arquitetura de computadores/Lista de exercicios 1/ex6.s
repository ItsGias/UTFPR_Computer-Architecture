.data

.text

	
		main: 
	
			li $v0,5
			syscall
			move $t0, $v0
			#faz o scanf


			li $t1, 10
			li $t2, 0
			#atribui os valores

			beq $t1, $t0, sair
			#Branch Equal para ver se t1 eh 10
			
			li $v0, 1
			move $a0, $t2
			syscall
			#printa o valor 0

			li $v0,10
			syscall
			#sai do programa

	
		sair:

			li $v0, 1
			move $a0, $t1
			syscall
			#printa o valor 10

			li $v0,10
			syscall
			#sai do programa
			
			

			