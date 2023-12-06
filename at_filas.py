fila = list(range(1, 6))

while True:
    entre = input('Precione "F" para adicionar alguém, "A" para remover, ou "S" para fechar: ')
    match entre:
        case 'F':
            fila.append(len(fila)+1)
            print(f'Atualmente a fila tem {len(fila)} pessoas.')
        case 'A':
            del fila[0]
            print(f'O proximo numero da fila é {fila[0]}')
            print(f'Atualmente a fila tem {len(fila)} pessoas.')
        case 'S':
            print('Você encerrou o programa!')
            break
    if entre != 'F' and entre != 'A' and entre != 'S':
        print('Opição Invalida!')