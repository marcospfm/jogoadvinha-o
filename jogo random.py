import random
import os

erros=0
sorteado=random.randrange(0,100)
jogador=int(input("escolha um numero: "))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("o numero é maior")
    elif(sorteado<jogador):
        print("o numero e menor")
    erros+=1
    jogador=int(input("escolha um numero: "))
    print("numero " + str(jogador) + ", voce acertou em " + str(erros+1) + "tentativas")