# Rock-paper-scissors
play rock paper scissor with the computer
import random
import time

def print_slow(palavra, atraso=0.04):
    for letra in palavra:
        print(letra, end='', flush=True)  # 'flush=True' garante que a saída seja exibida imediatamente
        time.sleep(atraso)
    print()

def play():
    user = input("What's your choice:  'r' for Rock, 'p' for Paper, 's' for Scissors\n")
    computer = random.choice(['r','p', 's']) 
    if user ==  computer:
        return 'Its\'s a tie '   
    if is_win(user, computer):
        return 'yeah, you won ;)))'
    return 'you lost hahaha'

def is_win(player, opponent):
    #return true if players win
    #r > s, s > p, p > r 
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
    or (player == 'p' and opponent == 'r'): 
        return True
    
print_slow(play())
