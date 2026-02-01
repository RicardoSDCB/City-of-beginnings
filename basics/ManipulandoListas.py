#Trabalhando com listas:

'''Uma lista é algo bem simples e de uso comum, mas trabalhar com elas é
que torna a coisa legal, aqui irão estar expostos algumas coisas que podemos
fazer para manipular listas:'''


#Listas para manipular:
random_numbers = [4, 5, 10, 17, 22, 123, 55, 45, 22, 24, 20]
amigos = [Gu, Bolinha, Efsu, Caetaninho, Ricardo]

-------------------------------------------------------------

#Mesclar duas listas em uma só:

amigos.extend(random_numbers) #com o comando .extend() nós juntamos duas listas

-------------------------------------------------------------

#Adiconar itens em uma lista:

amigos.append('Japones') #Com o comando .append() nós adicionamos itens na lista

-------------------------------------------------------------

#inserindo itens na lista em determinada posição

'''O comando .insert() por si só já adiciona itens na lista, mas para direcionar
ele em um espaço específico em que desejamos algo na lista, fazemos da seguinte
forma:'''

amigos.insert(1, 'Carol') '''Especificamos que no espaço 1 queremos adicionar o item
de nome 'Carol', todos os outros itens a frente do 1 irão andar uma casa para cima '''

-------------------------------------------------------------

#Removendo elementos:

amigos.remove('Ricardo') #Removemos o item cujo nome específico é 'Ricardo'

-------------------------------------------------------------

#Limpando listas:

amigos.clear() #Esse comando claramente limpará todo o conteúdo da lista.

-------------------------------------------------------------

#Removendo o último elemento da lista de maneira mais rápida:

amigos.pop() #Esse comando remove o último item adicionado na lista

-------------------------------------------------------------

#Localizando coisas na lista:

'''Para localizarmos valores em uma lista, seja qual for, usamos o comando
.index() que serve justamente para tal proposito:   '''

print(amigos.index('')) #Dentro da aspas digitamos o valor que queremos encontrar

-------------------------------------------------------------

#Contando quantas vezes algo se repete na lista:

print(amigos.count('')) #Dentro do parenteses, referenciamos o que queremos contar

-------------------------------------------------------------

#Embaralhando listas:

amigos.sort() #Comando que randomiza a lista

-------------------------------------------------------------

#Revertendo a ordem da lista:

amigos.reverse() #Inverte a ordem da lista colocando ela ao contrário

-------------------------------------------------------------

#Clonando listas:

amigos2 = amigos.copy() #Copia uma lista e coloca ela em outra

-------------------------------------------------------------

