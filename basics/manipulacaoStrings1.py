#Forma de adicionar aspas dentro de uma String sem fechar a mesma:

print('Para adicionar as aspas, basta usar a contra barra \"dessa forma\"')
#assim, na hora em que executar esse comando, ele irá mostrar as aspas normalmente

----------------------------------------------------------------------------------

#Manipulação de Strings:

frase = 'Apenas uma frase para ser usada como exemplo' #Frase usada para manipulação

-------------------------------------------------------------

#Função para deixar todas as letras maiúsculas e minúsculas:

print(frase.upper()) #Deixa todas as letras minúsculas

print(frase.lower()) #Deixa todas as letras minúsculas

-------------------------------------------------------------

#Função para verificar se uma String é ou não é maiúscula ou minúscula

print(frase.isupper()) #Verifica se a string está por inteira maiúscula

print(frase.islower()) #Verifica se a string está por inteira minúscula

-------------------------------------------------------------

#Agora algo interessante, podemos mesclar essas funções, veja:

print(frase.upper().isupper()) #Agora ela vai deixar em caixa alta e verificar

print(frase.lower().islower()) #O mesmo para caixa baixa

-------------------------------------------------------------

#Função para verificar QUANTAS LETRAS tem na palavra/frase:

print(len(frase)) #Função len com a frase desejada ou palavra entre parenteses

-------------------------------------------------------------

#Agora, como selecionar uma letra em específico? Simples, use a variável
#com colchetes:

print(frase[0]) #O número representa qual letra que você deseja saber

-------------------------------------------------------------

#Função index para encontrar algo específico na frase:

print(frase.index('usada')) '''A função irá localizar na frase onde está essa
palavra e irá retornar o número respectivo a isso. Também funciona para encontrar
letras'''

-------------------------------------------------------------

#Função para substituir palavras e/ou letras nas strings:

print(frase.replace('usada', 'utilizada')) #A esquerda a palavra que queremos
#substituir e a direita a palavra que entrará no lugar



