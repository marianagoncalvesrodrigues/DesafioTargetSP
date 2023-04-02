#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

a=1
b=0
c=0
i=0
lista = []
lista.append(0)
lista.append(1)
while i<15:
  c=a 
  a=a+b 
  b=c 
  print(a) 
  lista.append(a)
  i=i+1

numero_sorteado = input("escreva um numero aqui para verificar se pertence a sequencia de Fibonacci:")
if int(numero_sorteado) in lista:
  print("está na lista")
else:
  print("nao está na lista")
