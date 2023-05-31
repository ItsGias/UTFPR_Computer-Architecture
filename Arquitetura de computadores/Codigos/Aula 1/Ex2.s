.data

.text

	
	main:
		li $t0, 10
		li $t1, 20
		#ESTABELECE OS VALORES DE T0 E T1

		add $t0, 4
		sub $t1, 6 
		add $t3, $t1, $t0	
		# FAZ A SOMA E A SUBRACAO, E APOS ISSO SOMA T0 E T1

		li $v0, 1
		move $a0, $t3
		syscall
		#CHAMADA DE SISTEMA PARA PRINTAR O RESULTADO

		li $v0, 10
		syscall
		#FECHA O PROGRAMA