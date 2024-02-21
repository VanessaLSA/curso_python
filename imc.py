#Progama para calcular IMC
#Desenvolvido por Vanessa

print("*****************************************")
print("*          CALCULADORA DE IMC           *")
print("*****************************************")
print()


#Criação das variáveis
nome = ""
peso = 0
altura = 0.0
imc = 0.0


#ENTRADA DOS DADOS 
nome = input ("Digite o seu nome: ")
peso = int(input ("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))


#PROCESSAR OS VALORES PARA OBTER O IMC
imc  = peso / altura ** 2
if imc < 18.5 :
    situacao = ("Abaixo do peso! ")
elif imc > 18.5 and imc < 25.0:
    situacao = ("Peso normal! ")
if imc > 25 and imc < 30.0:
    situacao = ("Sobrepeso!")
if imc > 30 and imc < 35.0:
    situacao = ("Obesidade grau I ")
if imc > 35 and imc < 40.0:
    situacao = ("Obesidade grau II ")
if imc >= 40:
    situacao = ("Obesidade grau III ou mórbida")
    
#SAIDA DO PROCESSAMENTO

print()
print("***************************************")
print("*            RESULTADO                *")
print("*                                     *")
print("NOME: " + nome)
print("PESO: " + str(peso) + "Kg")
print("ALTURA: " + str(altura) + "m")
print("IMC: " + str(imc))
print("situação "+ situacao )




      
