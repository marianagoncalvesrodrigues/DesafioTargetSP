#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#O menor valor de faturamento ocorrido em um dia do mês;
#O maior valor de faturamento ocorrido em um dia do mês;
#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

from bs4 import BeautifulSoup 
  
with open('teste.xml', 'r') as f: 
    data = f.read() 
  
Bs_data = BeautifulSoup(data, "xml") 
b_unique = str(Bs_data.find_all('fevereiro'))
  
print(b_unique) 
newString = []
dias = 0
newString = b_unique.split("<, >, /", 29)

if(newString == "fevereiro"):
  dias = 28
else:
  dias = 30
soma = 0
newList = []
for item in newString:
  if(item > 1 and item < 29):
    newList.add(int(newString[item]))
    soma = int(newString[item]) + soma

media = soma/dias
contador = 0
for i in newList:
  if(newList[i] > media):
    contador = contador + 1
  else:
    continue

print("O maior faturamento do mes foi de: ")
print(max(newList))
print("O menor faturamento do mes foi de: ")
print(min(newList))
print("O numero de dias que teve um faturamento maior que a media mensal foi de: ")
print(contador)
