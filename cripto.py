#Cifragem de César 
print('---------------------')
print('Bem-vindo')
print('---------------------')
print('Esse é o cifra de César')
print('---------------------')
print('Você pode codificar e descodificar.')
print('E pode usar a rotação que quiser. (Rotação é quantos caracteres adiante ele vai substituir)')
print('Exemplo: (a) com rotação 3 vai ser (ã)')
print('---------------------')
caracte = ('aáàãâbcçdeéèêfghiíìjklmnoóòôõpqrstuúûùvwxyz0123456789') 
rot = int ( input ('Digite um valor de 1 à 52: ') ) 


def codificar (mensagem):
    m=''
    for i in mensagem:
        if i in caracte:
            i_index = caracte.index(i)
            m += caracte [(i_index + rot) % len(caracte)]
        else:
            m += i
    return m


def descodificar (mensagem):
    m = ''
    for i in mensagem:
        if i in caracte:
            i_index = caracte.index(i)
            m += caracte [(i_index - rot) % len(caracte)]
        else:
            m += i
    return m


def rodape ():
    print('---------------------')
    print('---------------------')
    print('Cifragem de César')
    print('---------------------')
    print('UNIP, 2020')
    print('---------------------')
    print('SI2P07')
    print('Projeto APS')
    print('---------------------')
    print('---------------------')



while True:
    coman = input ( 'O que deseja fazer? ' )
    if coman == 'codificar':
        msg = input ( 'Digite a mensagem: ' ).lower()
        cod = codificar (msg)
        print ('A mensagem codificada em rot', rot,'fica: ', cod)
    elif coman == 'descodificar':
        msg = input ( 'Digite a mensagem: ' )
        desc = descodificar (msg)
        print ('A mensagem descodificada em rot', rot,'fica: ',desc)
    else:
        print ( 'Comando inválido.' )
    rodape()
    fim = input ('Deseja continuar?')
    if fim == 'nao' or fim == 'não':
        print ( 'Fim do programa.' )
        break

