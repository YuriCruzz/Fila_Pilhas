pilha = list(range(1, 6))

while True:
    entre = input('Precione "E" para adicionar um Prato, "D" para remover, ou "S" para fechar: ')
    match entre:
        case 'E':
            pilha.append(len(pilha)+1)
            print(f'Atualmente a pilha tem {len(pilha)} pratos.')
        case 'D':
            fi_pilha = len(pilha)-1
            del pilha[fi_pilha]
            print(f'Atualmente a pilha tem {len(pilha)} pratos.')
        case 'S':
            print('Você encerrou o programa!')
            break
    if entre != 'E' and entre != 'D' and entre != 'S':
        print('Opição Invalida!')