.data

.text

	main: 
		
		li $t0, 10
		li $t1, 20

		add $t0, 4
		sub $t1, 6
		sub $t3, $t0, $t1

		li $v0, 1
		move $a0, $t3
		syscall

		li $v0, 10
		syscall