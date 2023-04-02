#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

palavra = "geladeira"
i=0
tam=len(palavra) -1

lista = list(palavra)
nova_lista = []

while tam>=i:
  carac = lista[tam]
  nova_lista.append(carac)
  tam=tam-1

palavra_invertida = ' '.join(nova_lista)

print(palavra_invertida)
