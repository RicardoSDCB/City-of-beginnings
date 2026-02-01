'''if statement '''

'''Uma das coisas mais comuns hein? Simbora'''

'''If é algo bem simples, como abrir, como fechar, como criar mais laços:'''

if comida == True:
    print('Faça algo.')
else:
    print('Não faça mais nada')
    
'''Esse if acima só possui apenas uma condição, portanto é bem simples, mas caso
queiramos mais condições atreladas a ela, usamos o elif'''

if comida == 'morango':
    print('morango é gostoso.')
elif comida == 'kiwi':
    print('kiwi não é tão gostoso assim...')
elif comida == 'lichia':
    print('Lichia é divina, meu deus.')
else:
    print('Apenas uma fruta qualquer...')
    
'''Assim fazemos várias condições, podemos adicionar quantas forem necessárias.'''

----------------------------------------------------

'''Também podemos colocar mais de uma condição em um único if:'''

if comida == True and suco == True: #Aqui vemos que duas condições precisam constar verdadeiras para valer
    print('Hmmm, comida e suquin')
    
    
'''Podemos também fazer o OU:'''

if comida == True or suco == True:
        print('Hmmm, comida ou suquin baum, ou então os dois bauns') #Aqui apenas uma das condições precisa ser verdadeira (ou ambas serem), para valer
 
----------------------------------------------------

'''Agora vai algo legal kkk, se você quer verificar um boolean, e quer verificar
o mesmo negativamente (não é _______), basta fazer da seguinte forma:'''

eh_alto == True

if not(eh_alto):
    print('Você não é alto')
'''Assim você consegue verificar se a pessoa não é alta apenas com o uso do NOT'''

'''O NOT, nega o que é verdadeiro (ou falso se a variável assim for), portanto
ele faz a verificação do oposto do boolean que aquela variável possui'''

----------------------------------------------------

'''Usando comparações em nossos if's'''