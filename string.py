# -*- coding: utf-8 -*-

# Para concatenar strings, usa-se o sinal de + :
ladoA = "Diego";
ladoB = "José";
nome = ladoA + " " + ladoB + "\n";

# Através da operação len, é possível checar o tamanho de uma string:
contar = len(nome);
print (contar);

# Há a possibilidade de se exibir certa posição de um item de um vetor;
# Deve-se atentar para o número de itens do vetor, para não chamar um item inexistente.
# É possível, também, imprimir parcialmente uma string:
print(ladoA[0] + ladoB[0]);
print(nome[0:2]);


#Como strings são objetos, strings são passiveis de serem atribuidas a métodos.
#P. ex, os métodos lower e upper, que deixam as letras em caixa baixa ou alta, respectivamente:

print(nome.lower());
print(nome.upper());

# A função strip também pode ser usada, neste caso para remover espaços e/ou caracteres especiais:

corte = nome.strip();
print (corte);

# Com a função split, é possível converter uma string em uma lista:

FIFA = "Janco Tiano";
FIFA = FIFA.split();
print(FIFA);

# Com a função find, posso fazer buscar dentro da minha string

busca = FIFA.find("T");
print(FIFA[busca:]);