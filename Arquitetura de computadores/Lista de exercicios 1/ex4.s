.data

.text

		
		main: 

				li $t0, 100
				sw $t0, 80($zero)
				li $t0, 200
				sw $t0, 160($zero)


		sair:
	
				li $v0, 10
				syscall