.data

.text

	main:
		
		li $t0, 5
		sw $t0, 40($zero)
		#atribui o valor 5 na posicao de memoria 10

		li $t0, 20
		sw $t0, 160($zero)
		#atribui o valor 5 na posicao de memoria 40

		lw $t0, 40($zero)
		lw $t1, 160($zero)
		#carrega os valores das posicoes 10 e 40 em t0 e t1

		
		add $t3, $t0, $t1
		#faz a soma dos valores presentes na posicoes 10 e 40 
		sw $t3, 400($zero)
		#salva o resultado na posicao 100 de memoria
		
		lw $t3, 400($zero)
		#carrega o valor presente na posicao 100 de memoria

		
		li $v0, 1
		move $a0, $t3
		syscall
		#imprime o resultado

		li $v0, 10
		syscall
		#fecha o programa
		
		
		