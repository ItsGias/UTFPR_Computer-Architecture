#   Grupo Simulador
#   Integrantes: Gian Lucas dos Reis, Gustavo Naoki Jodai Kurozawa e Lucas Ribeiro Penna Maroja.
#   códigos binarios teste
#
#   111000000000001010000001001100011000000101000011 exemplo de jump
#   1111000000000010100000010011000110000001010000111110111100000000 exmeplo jal com jump para voltar para o ra (loop)
#   00010001000000000000001100000000 exemplo sw e lw
#   0111000100100011 exemplo slt
#
#   Checkpoint 2

#   Checkpoint 3 - Fatorial
#   Verificar Not

import pickle
import sys

memoria = []
zero = 0
t0 = 0
t1 = 0
t2 = 0
a0 = 0
a1 = 0
a2 = 0
s0 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0
gp = 0
sp = 0
pc = 0
ra = 0

dict = {"0000" :zero,
    "0001" :t0,
    "0010" :t1,
    "0011" :t2,
    "0100" :a0,
    "0101" :a1,
    "0110" :a2,
    "0111" :s0,
    "1000" :s1,
    "1001" :s2,
    "1010" :s3,
    "1011" :s4,
    "1100" :gp,
    "1101" :sp,
    "1110" :pc,
    "1111" :ra}

# --------------------------------------------------------------------------------------------
# get registrador
# --------------------------------------------------------------------------------------------

def getReg(dict, reg):
    for key, values in dict.items():
        if key == reg:
            return dict[reg]
        
# --------------------------------------------------------------------------------------------
# Altera registrador
# --------------------------------------------------------------------------------------------

def alterarReg(dict, reg, valor):
    for key, values in dict.items():
        if key == reg:
            dict[reg] = valor
        
    return dict

# --------------------------------------------------------------------------------------------
# Operacao R
# --------------------------------------------------------------------------------------------

def opR(dados, op):
    if op == "0010":
        print("Instrucao: ADD")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]

        alterarReg(dict, regd, getReg(dict, regs)+getReg(dict, reg2))

       # print(getReg(dict, regd))
    elif op == "0011":
        print("Instrucao: SUB")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]

        alterarReg(dict, regd, getReg(dict, regs)-getReg(dict, reg2))

       # print(getReg(dict, regd))

    elif op == "0100": #AND 0101 0110
        print("Instrucao: AND")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]

        binario1 = bin(getReg(dict, regs))
        binario2 = bin(getReg(dict, reg2))
        binario1 = binario1[2:]
        binario2 = binario2[2:]
        
        while len(binario1) < 4:
            binario1 = "0"+binario1 

        while len(binario2) < 4:
            binario2 = "0"+binario2

        binario3 = []
        for x in range(0, 4):
            binario3.append(int(binario1[x], 2) & int(binario2[x], 2)) 

        binario3 = ''.join(map(str, binario3))

        alterarReg(dict, regd, int(binario3, 2))

    elif op == "0101": #OR
        print("Instrucao: OR")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]

        binario1 = bin(getReg(dict, regs))
        binario2 = bin(getReg(dict, reg2))
        binario1 = binario1[2:]
        binario2 = binario2[2:]
        while len(binario1) < 4:
            binario1 = "0"+binario1 

        while len(binario2) < 4:
            binario2 = "0"+binario2

        binario3 = []
        for x in range(0, 4):
            binario3.append(int(binario1[x], 2) | int(binario2[x], 2)) 
        
        binario3 = ''.join(map(str, binario3))

        alterarReg(dict, regd, int(binario3, 2))

    elif op == "0110": #XOR
        print("Instrucao: XOR")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]

        binario1 = bin(getReg(dict, regs))
        binario2 = bin(getReg(dict, reg2))
        binario1 = binario1[2:]
        binario2 = binario2[2:]
        while len(binario1) < 4:
            binario1 = "0"+binario1 

        while len(binario2) < 4:
            binario2 = "0"+binario2

        binario3 = []
        for x in range(0, 4):
            binario3.append(int(binario1[x], 2) ^ int(binario2[x], 2)) 
        
        binario3 = ''.join(map(str, binario3))

        alterarReg(dict, regd, int(binario3, 2))

    elif op == "0111": # SLT
        print("Instrucao: SLT")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]

        if getReg(dict, regs) < getReg(dict, reg2):
            alterarReg(dict, regd, 1)
        else:
            alterarReg(dict, regd, 0)

    elif op == "1010":
        print("Instrucao: MUL")
        regs = dados[4:8]
        reg2 = dados[8:12]
        regd = dados[12:16]
        
        alterarReg(dict, regd, getReg(dict, regs) * getReg(dict, reg2))

    return

# --------------------------------------------------------------------------------------------
# Operacao I
# --------------------------------------------------------------------------------------------

def opI(dados, op):
    if op == "1000":
        print("Instrucao: ADDI")
        regs = dados[4:8]
        regd = dados[8:12]
        binario = dados[12:16]

        alterarReg(dict, regd, getReg(dict, regs)+int(binario, 2))

        #print(getReg(dict, regd))
    elif op == "1001":
        print("Instrucao: SHIFT")
        regs = dados[4:8]
        regd = dados[8:12]
        binario = int(dados[12:16], 2)

        valor = bin(getReg(dict, regs))

        rotacao = list(valor[binario:] + valor[:binario])
        rotacao.pop(0)

        for x in range(binario):
            rotacao[0-binario+x] = '0'

        rotacao = "".join(rotacao)
        
        alterarReg(dict, regd, int(rotacao, 2))
        #print(getReg(dict, regd))

    elif op == "1100":
        print("Instrucao: BEQ")
        regs = dados[4:8]
        regd = dados[8:12]
        
        if getReg(dict, regs) == getReg(dict, regd):
            deslocamento = int(dados[12:16], 2)
            valor = getReg(dict, regd)

            alterarReg(dict, "1110", deslocamento-1) 


    elif op == "1101":
        print("Instrucao: BLT")
        regs = dados[4:8]
        regd = dados[8:12]

        if getReg(dict, regs) < getReg(dict, regd):
            deslocamento = int(dados[12:16], 2)

            alterarReg(dict, "1110", deslocamento-1) 

    elif op == "1011":
        print("Instrucao: LUI")
        regs = dados[4:8]
        valor = int(dados[8:16], 2)
        
        alterarReg(dict, regs, valor)

    return

# --------------------------------------------------------------------------------------------
# Operacao J
# --------------------------------------------------------------------------------------------

def opJ(dados, op):
    if op == "1110":
        print("Instrucao: J")
        regd = dados[4:8]
        deslocamento = int(dados[8:16], 2)
        valor = getReg(dict, regd)

        alterarReg(dict, "1110", deslocamento + valor -1) 

    elif op == "1111":
        print("Instrucao: JAL")
        alterarReg(dict, "1111", getReg(dict, "1110"))

        regd = dados[4:8]
        deslocamento = int(dados[8:16], 2)

        valor = getReg(dict, regd)

        alterarReg(dict, "1110", deslocamento + valor -1) 

    return

# --------------------------------------------------------------------------------------------
# Operacao LS
# --------------------------------------------------------------------------------------------

def opLS(dados, op):
    if op == "0001":
        print("Instrucao: SW")
        regs = dados[4:8]

        global memoria

        memoria.append(getReg(dict, regs))
        alterarReg(dict, "1101", getReg(dict, "1101")+1)

    elif op == "0000":
        print("Instrucao: LW")
        regs = dados[4:8]
        pointer = dados[8:12]
        deslocamento = int(dados[12:16], 2)

        alterarReg(dict, regs, memoria[deslocamento])

    return

# --------------------------------------------------------------------------------------------
# Verifica qual a operação
# --------------------------------------------------------------------------------------------

def verificaOp(dados):
    op = dados[0:4]
    if op == "0010" or op == "0011" or op == "0100" or op == "0101" or op == "1010" or op == "0110" or op == "0111":
        opR(dados, op)
    elif op == "1000" or op == "1001" or op == "1011" or op == "1100" or op == "1101":
        opI(dados, op)
    elif op == "1110" or op == "1111":
        opJ(dados, op)
    elif op == "0000" or op == "0001":
        opLS(dados, op)
    else:
        sys.exit("Warning: operacao invalida")
    return

# --------------------------------------------------------------------------------------------
# Separa as instruções
# --------------------------------------------------------------------------------------------

def separaInstrucao(entrada, dados):
    x=0
    while x < len(entrada):
        dados.append(entrada[x:x+16])
        x = x+16


# --------------------------------------------------------------------------------------------
# Formata Registadores
# --------------------------------------------------------------------------------------------

def formataReg(dict):
    
    print(
        "\nRegistradores:" +
        "\nzero = " + str(getReg(dict, "0000")) + "\nt0 = " + str(getReg(dict, "0001")) + "\nt1 = " + str(getReg(dict, "0010")) + "\nt2 = " + str(getReg(dict, "0011")) +
        "\na0 = " + str(getReg(dict, "0100")) + "\na1 = " + str(getReg(dict, "0101")) + "\na2 = " + str(getReg(dict, "0110")) + "\ns0 = " + str(getReg(dict, "0111")) +
        "\ns1 = " + str(getReg(dict, "1000")) + "\ns2 = " + str(getReg(dict, "1001")) + "\ns3 = " + str(getReg(dict, "1010")) + "\ns4 = " + str(getReg(dict, "1011")) +
        "\ngp = " + str(getReg(dict, "1100")) + "\nsp = " + str(getReg(dict, "1101")) + "\npc = " + str(getReg(dict, "1110")) + "\nra = " + str(getReg(dict, "1111")) + "\n"
        "------------------------------\n"
        )
    
    return

# --------------------------------------------------------------------------------------------
# Verifica Registradores
# --------------------------------------------------------------------------------------------

def verificaReg(input):
    
    if input.lower() == "$zero":
        return "0000"
    elif input.lower() == "$t0":
        return "0001"
    elif input.lower() == "$t1":
        return "0010"
    elif input.lower() == "$t2":
        return "0011"
    elif input.lower() == "$a0":
        return "0100"
    elif input.lower() == "$a1":
        return "0101"
    elif input.lower() == "$a2":
        return "0110"
    elif input.lower() == "$s0":
        return "0111"
    elif input.lower() == "$s1":
        return "1000"
    elif input.lower() == "$s2":
        return "1001"
    elif input.lower() == "$s3":
        return "1010"
    elif input.lower() == "$s4":
        return "1011"
    elif input.lower() == "$gp":
        return "1100"
    elif input.lower() == "$sp":
        return "1101"
    elif input.lower() == "$pc":
        return "1110"
    elif input.lower() == "$ra":
        return "1111"
    else:
        sys.exit("Warning: " + input + " registrador invalido")
    
# --------------------------------------------------------------------------------------------
# Instruções do Usuário
# --------------------------------------------------------------------------------------------

def instrucaoUsuario(dict):
    
    tipo = input("Informe qual a instrucao: ")
    opcode = ""
    if(tipo.lower() == "add"):
        opcode = opcode + "0010"
    elif(tipo.lower() == "sub"):
        opcode = opcode + "0011"
    elif(tipo.lower() == "addi"):
        opcode = opcode + "1000"
    elif(tipo.lower() == "shift"):
        opcode = opcode + "1001"
    elif(tipo.lower() == "and"):
        opcode = opcode + "0100"
    elif(tipo.lower() == "or"):
        opcode = opcode + "0101"
    elif(tipo.lower() == "mul"):
        opcode = opcode + "1010"
    elif(tipo.lower() == "xor"):
        opcode = opcode + "0110"
    elif(tipo.lower() == "slt"):
        opcode = opcode + "0111"
    elif(tipo.lower() == "lw"):
        opcode = opcode + "0000"
    elif(tipo.lower() == "sw"):
        opcode = opcode + "0001"
    elif(tipo.lower() == "lui"):
        opcode = opcode + "1011"
    elif(tipo.lower() == "beq"):
        opcode = opcode + "1100"
    elif(tipo.lower() == "blt"):
        opcode = opcode + "1101"
    elif(tipo.lower() == "j"):
        opcode = opcode + "1110"
    elif(tipo.lower() == "jal"):
        opcode = opcode + "1111"
    else:
        print("WARNING: instrucao invalida, digite 0 e digite novamente a instrucao")
        return
    
    if opcode == "0010" or opcode == "0011" or opcode == "0100" or opcode == "0101" or opcode == "1010" or opcode == "0110" or opcode == "0111": #R
        regs = input("Informe o Regs: ")
        regs = verificaReg(regs)
        
        reg2 = input("Informe o Reg2: ")
        reg2 = verificaReg(reg2)
        
        regd = input("Informe o Regd: ")
        regd = verificaReg(regd)
        
        opcode = opcode+regs+reg2+regd
        
    elif opcode == "1000" or opcode == "1001" or opcode == "1100" or opcode == "1101": #I
        regs = input("Informe o Regs: ")
        regs = verificaReg(regs)
        
        regd = input("Informe o Regd: ")
        regd = verificaReg(regd)
        
        const = input("Informe a Const: ")
        
        if int(const) > 15:
            sys.exit("Warning: a constante nao pode ser maior que 15")
        
        const = bin(int(const))
        const = const[2:]
        while len(const) < 4:
            const = "0"+const
        
        
        opcode = opcode+regs+regd+const
        
    elif opcode == "1110" or opcode == "1111" or opcode == "1011": #J
        regd = input("Informe o Regd: ")
        regd = verificaReg(regd)
        
        const = input("Informe a Const: ") 
        
        if int(const) > 255:
            sys.exit("Warning: a constante nao pode ser maior que 255")
        
        const = bin(int(const))
        const = const[2:]
        while len(const) < 8:
            const = "0"+const
            
        opcode = opcode+regd+const
        
        
    elif opcode == "0000" or opcode == "0001": #LS
        regs = input("Informe o Regs: ")
        regs = verificaReg(regs)
        
        reg2 = input("Informe o Reg2: ")
        reg2 = verificaReg(reg2)
        
        regd = input("Informe o Regd: ")
        regd = verificaReg(regd)
        
        opcode = opcode+regs+reg2+regd
    
    return opcode

# --------------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------------
def main():

    verifica = int(input("Voce deseja utilizar o programa com arquivos prontos ? [1 - SIM] [2 - NAO]: "))

    global dict

    if(verifica == 1):
        
        with open("arquivo.bin", "wb") as arquivo:
            dados = "10110100000001010010010000000101101100010000000100110101000101011100010100011000101001010100010011100000000000111011000100000001"
            pickle.dump(dados, arquivo)

        with open("arquivo.bin", "rb") as arquivo:
            entrada=(pickle.load(arquivo))

        dados = []
        separaInstrucao(entrada, dados)

        
        print(dados)
        while(getReg(dict, "1110") != len(dados)):
            verificaOp(dados[getReg(dict, "1110")])
            alterarReg(dict, "1110", getReg(dict, "1110")+1)
            formataReg(dict)
            
    elif(verifica == 2):
        parar = 0
        opcode = ""
        while(parar == 0):
            if parar != 0:
                break   
            opcode = opcode+instrucaoUsuario(dict)
            
            parar = int(input("Para encerrar o programa digite 1, caso queira continuar digite 0: "))

        with open("arquivo.bin", "wb") as arquivo:
                pickle.dump(opcode, arquivo)

        with open("arquivo.bin", "rb") as arquivo:
            entrada=(pickle.load(arquivo))

        dados = []
        separaInstrucao(entrada, dados)

        #dict = alterarReg(dict, "0001", 15)
        #dict = alterarReg(dict, "0010", 6)
        print(dados)
        while(getReg(dict, "1110") != len(dados)):
            verificaOp(dados[getReg(dict, "1110")])
            alterarReg(dict, "1110", getReg(dict, "1110")+1)
            formataReg(dict)
        
    else:
        print("Opcao invalida")

if __name__ == "__main__":
    main()