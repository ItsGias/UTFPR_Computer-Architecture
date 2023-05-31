.data

.text

		main:
			
			li $v0, 5
			syscall
			move $t0, $v0
			#recebe o primeiro inteiro

	 		li $v0, 5
			syscall
			move $t1, $v0
			#recebe o segundo inteiro

			


			beq $t0, $t1, igual
			#compara se os 2 valores sao iguais

			slt $s0, $t0, $t1
			#compara se t0 eh menor que t1
			bne $s0, $zero, bigtum
			#se slt t1 for maior q t0 o codigo vai para bigtum

			li $v0, 1
			move $a0,$t0
			syscall
			#printa o resultado

			li $v0, 10
			syscall
			#Fecha o programa



			

		bigtum:
			
			li $v0, 1
			move $a0,$t1
			syscall
			#printa o resultado

			li $v0, 10
			syscall
			#Fecha o programa


		igual:
			
			li $t2, -111
			#atribui -111 a t2
			
			li $v0, 1
			move $a0,$t2
			syscall
			#printa o resultado

			li $v0, 10
			syscall
			#Fecha o programa
		