#CÁLCULO DA MÉDIA DOS ALUNOS


print("******MÉDIA FINAL******")
print("***********************")
print()

nome = input("Digite o seu nome")
nota_do_primeiro_bimestre = float (input ("nota 1: "))
nota_do_segundo_bimestre = float (input ("nota 2: "))
nota_do_terceiro_bimestre = float (input ("nota 3 "))
nota_do_quarto_bimestre = float (input ("nota 4 "))
media_final = (nota_do_primeiro_bimestre + nota_do_segundo_bimestre + nota_do_terceiro_bimestre + nota_do_quarto_bimestre) / 4
if media_final >= 7.0:
    
    
    print (nome + ",sua nota final é " + str(media_final))
    print (f"{nome},você foi aprovado! sua média é {media_final}")
elif media_final <5:
    print (f"{nome}, você foi reprovado! sua média é {media_final}")
    

else:
    print (f"{nome}, você está de recuperação! sua média é {media_final}")
    
