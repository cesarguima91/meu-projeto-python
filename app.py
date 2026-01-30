from datetime import datetime

nome = input("Olá, qual é o seu nome? ")
hora_atual = datetime.now().strftime("%H:%M")

print(f"\nOlá, {nome}! Seja bem-vindo(a).")
print(f"Agora são {hora_atual}.")
