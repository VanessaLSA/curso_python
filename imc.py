x''# Programa para calcular IMC
# Desenvolvido por Celso

print("****************************************")
print("*        CALCULADORA DE IMC            *")
print("****************************************")
print()

# CRIAÇÃO DAS VARIÁVEIS
nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC
imc = peso / altura ** 2

# SAÍDA DO PROCESSAMENTO
print()
print("*******************************")
print("*          RESULTADO          *")
print("*******************************")
print("*                             *")
print("NOME: " + nome)
print("PESO: " + str(peso) + "Kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))
