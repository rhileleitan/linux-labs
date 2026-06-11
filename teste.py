print ('Olá, amigo')
print ('')

minha_lista = []

while True:
    texto = input('Digite qualquer coisa: ')

    if texto != '':
        minha_lista.append (texto)
        print (f'Sua lista tem {minha_lista} itens inseridos.')
    else:
        print ('Você deve digitar alguma coisa.')
