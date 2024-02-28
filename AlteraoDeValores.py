import time

def print_com_atraso(palavra, atraso=0.05):
    for letra in palavra:
        print(letra, end='', flush=True)  # 'flush=True' garante que a saída seja exibida imediatamente
        time.sleep(atraso)
    print()
valor_disponivel = 1000
boas_vindas = (f'Olá bem vindo ao banco ceco, você tem disponivel {valor_disponivel}, quanto deseja sacar?')
print_com_atraso(boas_vindas)
valor_saque = int(input('digite o valor: '))
valor_restante_na_conta = valor_disponivel - valor_saque
resultado = (f'você sacou {valor_saque}, seu saldo atual é de: {valor_restante_na_conta}')
print_com_atraso(resultado)#




