.data

.text

	if:

		li $t0, 2
		li $t1, 10
		li $t2, 50
		
		slt $s0, $t0, $zero
		#set less than
		bne $s0, $zero, else
		#branch not equal
		bgt $t1, $t2, else
		#branch greater than
		li $t3, 1

	else: 
		li $v0, 1	
		move $a0, $t3
		syscall
		
		li $v0, 10
		syscall




		
	