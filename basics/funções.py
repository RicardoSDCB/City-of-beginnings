'''Funções em Python'''

'''Funções são uma das coisas mais importantes na hora de programar, sendo um 
dos cores da programação, elas são muito usadas quando nós temos que realizar um
processo repetidas vezes por exemplo, e usando uma função já criada e determinada
por nós, podemos chamar ela quantas vez quisermos e ela irá dar conta do trabalho!'''


-------------------------------------------------------------

                '''Como criar uma função:'''
    ''' 'def' é o termo usado para criarmos uma função. '''

def diga_oi():
    print('Olá ^-^') 

-------------------------------------------------------------
#Chamando a nossa função:

diga_oi() #Só por fazer isso, o código irá printar automáticamente a mensagem

-------------------------------------------------------------
'''Funções possuem mais do que isso, como no caso, quando criamos uma função,
usamos o "def nome_funcao()" e aí está, mas conseguimos ir além, pedindo uma 
informação para o nosso usuário. Mas como fazer isso? Simples, usamos a seguinte
maneira de escrever a função:'''

def ola(nome) '''Dentro dos parenteses irá o que pode ser considerado uma variável (é chamado de parâmetro), apenas não definimos o que ela irá receber, só na hora de chamar a função que ela ganhará uma "identidade"'''
    print(f'Olá {nome}')
    
ola('Rii') '''Devemos agora escrever dentro dos parenteses da função, o que
pedimos, no caso o nome.
    O resultado desse print, será: Olá Ricardo
'''

-------------------------------------------------------------

'''Conseguimos pedir mais de um parametro para a função, sendo assim:'''

def ola_idade(nome, idade):
    print(f'Olá {nome}, você possui {} anos.')

ola_idade('Ricardo', '20') #É assim que passamos mais de uma informação

------------------------------------------------------------- 


