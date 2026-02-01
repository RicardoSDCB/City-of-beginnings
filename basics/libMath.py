#Manipulação de números:
num = 10
-------------------------------------------------------------

'''Aqui vai uma pequena explicação, para printar números junto com textos o 
Python apresenta alguns problemas, para tal, precisamos converter o número que
queremos printar em conjunto com o texto em uma String também, assim: '''

print(num+'texto qualquer') #Isso retornará um erro

print(str(num)+'texto qualquer') #Isso por sua vez dará certo pela conversão
#de int para str
 
'''No entanto, se você fizer o uso de uma f string (ou seja, print(f'')), você
não irá ter que lidar com esse erro, sendo muito mais simples'''

print(f'{num} texto qualquer') #Isso irá funcionar normalmente

-------------------------------------------------------------

'''Pra ser franco, nessa parte da aula, apenas conceitos muito básicos foram
mencionados e por tal motivo eu resolvi não mencioná-los aqui.

O importante de se mencionar, acredito eu, foi a menção válida da lib math!
Uma lib matemática muito útil e importante.'''

-------------------------------------------------------------


