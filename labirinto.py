print ("Você está na sala 1")

opcao = int(input("Escolha a proxima sala, 1 para direita e 2 para esquerda"))

#como definir as salas
sala = 1
LIMITE_INTERAÇÕES = 7

while(sala <= LIMITE_INTERAÇÕES):
    if (opcao == 1):    
        sala = sala + 2
    elif (opcao == 2):
        sala = sala + 1
print("Você está na sala", sala)
opcao = int(input("Escolha a proxima sala, 1 para direita e 2 para esquerda"))

    


