#Falando sobre Tuplas em Python:

'''Começando com algumas informações importantes. Uma Tupla é praticamente igual
a uma lista, no entanto ela tem algumas particularidades, começando com a sua
criação'''

#Criando uma tupla:

coordenadas = (10, 5) #Usamos parenteses para criar uma tupla

-------------------------------------------------------------

'''Tuplas possuem valores IMUTÁVEIS, não podemos alterar ela após sua criação.
Criada uma vez, nenhuma alteração é possível, ela é o que foi feita pra ser.'''

-------------------------------------------------------------
'''Podemos printar tuplas de maneira inteira ou então indexando o que queremos
da seguinte maneira:'''

print(coordenadas) #printamos a tupla inteira

print(coordenadas[1]) #printamos apenas o valor localizado em 1

-------------------------------------------------------------

'''Também é possível criar uma lista de tuplas, que pode vir a ter sua utilidade:'''

coordenadasAvulcas = [(100, 255), (12, 36), (15, 05), (27, 02)]

'''Colocando as tuplas dentro de uma lista, temos uma lista que podem ser adicio_
nadas mais tuplas, mas claro, não podemos modificar as mesmas'''

-------------------------------------------------------------

