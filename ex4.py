#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

soma =  67836.43+36678.66+29229.88+27165.48+19849.53

list = [SP, RJ, MG, ES, Outros]
for i in list:
  if(list.index(i) == 0):
    print("SP: ")
    x = (i*100)/soma
    x = str(x)
    print("A porcentagem foi de: " + x + "%")
  elif(list.index(i) == 1):
    print("RJ: ")
    x = (i*100)/soma
    x = str(x)
    print("A porcentagem foi de: " + x + "%")
  elif(list.index(i) == 2):
    print("MG: ")
    x = (i*100)/soma
    x = str(x)
    print("A porcentagem foi de: " + x + "%")
  elif(list.index(i) == 3):
    print("ES: ")
    x = (i*100)/soma
    x = str(x)
    print("A porcentagem foi de: " + x + "%")
  else:
    print("Outros: ")
    x = (i*100)/soma
    x = str(x)
    print("A porcentagem foi de: " + x + "%")
  

  
