import random

LIMITE_INTERAÇÕES = 7

sala = 1
cont = 1

print("Você está na sala: 1")

def resolve_salas(sala, opcao):
  if sala == 8 and opcao == 1:
    return 9
  elif sala == 8 and opcao == 2:
    sala = random.choices([1,2,3,4,5])
    return sala
  elif opcao == 1 and sala != 8:
    sala += 1
    return sala
  elif opcao == 2 and sala != 8:
    sala += 2
    return sala


while(cont <= LIMITE_INTERAÇÕES):
    opcao = int(
      input("--- Escolha seu caminho ---\n [1] - Caminho Vermelho\n [2] - Caminho Preto\n Opcao: ")
    )
    sala = resolve_salas(sala, opcao)
    if sala == 9:
      print("Sala 9 atinginda! Parabens voce venceu!")
      break
    elif sala == 6:
      print("O caminho vermelho esta bloqueado\nSua unica opção é o caminho preto")
      print("[x] Caminho Preto\n")
      sala = 8
    print("Você está na sala: ", sala)
    cont += 1