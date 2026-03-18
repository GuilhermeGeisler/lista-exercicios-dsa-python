import random

print("-------------------------------")
print("--- Jokenpo (CPU vs Player) ---")
print("-------------------------------")
print("Bem-vindo ao Jokenpo! Escolha sua jogada:")

opcoes = ("pedra", "papel", "tesoura")
print(f"Opções disponíveis: {opcoes}")
print("-" * 25)

jogada_cpu = random.choice(opcoes)
jogada_jogador = input("Digite sua jogada: ").lower().strip()

print("-" * 25)
print(f"Jogada do CPU: {jogada_cpu}")
print(f"Jogada do Jogador: {jogada_jogador}")
print("-" * 25)

if jogada_jogador == jogada_cpu:
    print("Empate!")
elif (jogada_jogador == "pedra" and jogada_cpu == "tesoura") or \
     (jogada_jogador == "papel" and jogada_cpu == "pedra") or \
     (jogada_jogador == "tesoura" and jogada_cpu == "papel"):
    print("Você venceu!")
else:
    print("CPU venceu!")

print("\n--- Fim de Jogo ---")