'''Trabalhanco com dicionários'''

'''Dicionários... hmm, bom, já está bem claro que para criar listas usamos [], 
para criar tuplas usamos () e por fim, para criar um dicionário, iremos usar {}.'''

'''Eu irei criar aqui um dicionário que irá nos conveter siglas em nomes completos
e para efeito demonstrativo, iremos usar os dias da semana'''

semanaConvercoes = { #Apenas refrizando, é assim que se cria um dicionário :D
    'Dom': 'Domingo',
    'Seg': 'Segunda',
    'Ter': 'Terça',
    'Qua': 'Quarta',
    'Qui': 'Quinta',
    'Sex': 'Sexta',
    'Sab': 'Sábado'
}

'''Quando você deseja acessa um dos itens desse dicionário, podemos fazê-lo
das seguintes maneiras:'''

print(semanaConvercoes['Ter']) '''Essa é a primera maneira de se selecionar e 
mostrar um dos itens do dicionário'''

print(semanaConvercoes.get('Seg')) '''O legal de usar essa função .get, é que
nós podemos setar um valor vazio se a chave procurada não for encontrada.

Isso é muito simples, irei mostrar:'''

print(semanaConvercoes.get('Luv', 'Não é uma chave válida')

'''Fazendo dessa maneira o .get, caso o valor pedido não exista, retornaremos a
mensagem a seguir, que no caso se trata da mensagem 'Não é uma chave válida'.'''




'''Lembrando que as chaves adicionadas no dicionário, não precisam começar com
strings, como foi feito na de cima, podem iniciar com ints'''

numDict = {
    0 = 'Segunda'
    1 = 'Terça'
    2 = 'Quarta'
    3 = 'Quinta'
    4 = 'Sexta'
    5 = 'Sábado'
    6 = 'Domingo'
}

'''Existem outras maneiras de se chamar uma chave de um dicionário, mas foram 
essas passadas nesse curto vídeo, mais anotações podem vir depois'''

