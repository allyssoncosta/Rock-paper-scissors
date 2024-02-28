from datetime import datetime
import time
import random
import webbrowser

data_hora_atual = datetime.now()

ano = data_hora_atual.year
mes = data_hora_atual.month
dia = data_hora_atual.day
hora = data_hora_atual.hour
minuto = data_hora_atual.minute
segundo = data_hora_atual.second

def print_com_atraso(palavra, atraso=0.04):
    for letra in palavra:
        print(letra, end='', flush=True)  # 'flush=True' garante que a saída seja exibida imediatamente
        time.sleep(atraso)
    print()

frases_negativas = [
"seu merdinha do caralho, só fez isso hoje? vai proporcionar o que pra tua mãe, maldito desgraçado", 
"nss.. pqp.. vou nem comentar. Um obeso faria melhor", 
"horrivel, quer ser o melhor assim como?", 
"hahaha, voce é um lixo. ass: David goggins", 
"pessimo kk tem nem o que comentar."
]
frases_positivas = [
 "hmm, muito bom, tá mais proximo do que ontem",
 "muito bom, siga firme. ass: david goggins",
 "brabo brabo, ta no caminho",
 "boa caralho, voce ta passando deles."   
]

frase_aleatoria_negativa_estudo = random.choice(frases_negativas)
frase_aleatoria_positiva_estudo = random.choice(frases_positivas)

frase_aleatoria_negativa_cardio = random.choice(frases_negativas)
frase_aleatoria_positiva_cardio = random.choice(frases_positivas)

frase_aleatoria_negativa_treino = random.choice(frases_negativas)
frase_aleatoria_positiva_treino = random.choice(frases_positivas)

frase_aleatoria_negativa_alimento = random.choice(frases_negativas)
frase_aleatoria_positiva_alimento = random.choice(frases_positivas)

boas_vindas = (f'olá, seja bem vindo, gostariamos de saber como foi o seu desempenho no dia: {dia}/{mes}/{ano}... que no caso é hoje')
print_com_atraso(boas_vindas)
treino = input('você treinou hoje: ')
comida = input('comeu saldavel: ')
cardio = input('fez cardio hoje: ')
estudo = input('estudou hoje: ')

resultado_treino = treino
resultado_comida = comida
resultado_cardio = cardio
resultado_estudo = estudo


if resultado_treino.lower() == 'sim':
    print_com_atraso(f'em relação ao seus treinos: {frase_aleatoria_positiva_treino}')
elif resultado_treino.lower() == 'não':
    print_com_atraso(f'em relação ao seus treinos: {frase_aleatoria_negativa_treino}')


if resultado_estudo.lower() == 'sim':
    print_com_atraso(f'em relação ao seus estudos: {frase_aleatoria_positiva_estudo}')
elif resultado_estudo.lower() == 'não':
    print_com_atraso(f'em relação ao seus estudos: {frase_aleatoria_negativa_estudo}')


if resultado_comida.lower() == 'sim':
    print_com_atraso(f'em relação a sua alimentação: {frase_aleatoria_positiva_alimento}')
elif resultado_comida.lower() == 'não':
    print_com_atraso(f'em relação a sua alimentação:{frase_aleatoria_negativa_alimento}')


if resultado_cardio.lower() == 'sim':
    print_com_atraso(f'em relação ao seu cardio: {frase_aleatoria_positiva_cardio}')
elif resultado_cardio.lower() == 'não':
    print_com_atraso(f'em relação a sua cardio:{frase_aleatoria_negativa_cardio}')

link_do_video = "https://www.youtube.com/shorts/IicbiwTAslE"
print('acho que você precisa disso aqui...')
webbrowser.open(link_do_video)
