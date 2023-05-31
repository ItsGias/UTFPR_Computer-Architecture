.data

.text

	main: 
			li $t0, 5
			sw $t0, 40($zero)
			#ATRIBUI UM VALOR A T0 E DEPOIS SALVA ELE NO ENDERECO DE MEMORIA 10

			li $t1, 20
			sw $t1, 160($zero)
			#ATRIBOU UM VALOR A T1 E DEPOIS SALVA ELE NO ENDERECO DE MEMORIA 40

			lw $t0, 40($zero)
			lw $t1, 160($zero)
			#CARREGA O VALOR NO ENDERECO DE MEMORIA 10 EM T0 E CARREGA O VALOR NO ENDERECO DE MEMORIA 40 EM T1

			add $t3, $t0, $t1
			sw $t3, 400($zero)
			#FAZ A SOMA DE T0 E T1 E SALVA O RESULTADO NO ENDERECO DE MEMORIA 100


			

			li $v0, 1
			move $a0, $t3
			#CHAMADA RECURSIVA PARA EXIBIR O RESULTADO

			li $v0, 10
			syscall
			#CHAMADA DE SISTEMA PARA FECHAR O PROGRAMA