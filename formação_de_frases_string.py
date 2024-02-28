import time

def print_com_atraso(palavra, atraso=0.02):
    for letra in palavra:
        print(letra, end='', flush=True)  # 'flush=True' garante que a saída seja exibida imediatamente
        time.sleep(atraso)
    print()

name_user = input('\nqual o seu nome: ')
verb1 = input('um esporte')
pers1 = input('pessoa que você não gosta: ')
pers2 = input('pessoa que voce gosta bastante: ')
pers3, pers4 = 'blabla', "blublu"

print_com_atraso(f'{name_user}, voce se parece tao cansado e abatido, na ultima vez que voce {verb1}, você o fez tao desanimado, parecia até {pers1}, lembrese da sua insipiração, ela tem um nome, e seu nome é {pers2}, e ele não gostaroia disso')

print_com_atraso(pers3, pers4)