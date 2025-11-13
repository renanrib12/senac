#%%
import random
# --- Variáveis de Controle ---
vitorias_usuario = 0
vitorias_computador = 0
empates = 0

opcoes = ['pedra', 'papel', 'tesoura']

print("--- JOGO: PEDRA, PAPEL, TESOURA ---")
print("O jogo continua até você vencer 3 rodadas!")

# --- Loop Principal do Jogo ---
# O loop continua enquanto o usuário não tiver 3 vitórias
while vitorias_usuario < 3:
    print("\n------------------------------")
    print(f"PLACAR ATUAL: Você {vitorias_usuario} x {vitorias_computador} Computador | Empates: {empates}")
    
    # 1. Pede a entrada do usuário
    escolha_usuario = input("Escolha (Pedra, Papel ou Tesoura): ").strip().lower()
    
    # 2. Escolha do computador (aleatória)
    escolha_computador = random.choice(opcoes)

    # 3. Verifica a entrada do usuário
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Por favor, digite 'pedra', 'papel' ou 'tesoura'.")
        continue  # Volta para o início do loop

    print(f"Você escolheu: {escolha_usuario.capitalize()}")
    print(f"O computador escolheu: {escolha_computador.capitalize()}")

    # 4. Determina o vencedor da rodada (if/elif/else)
    
    # Caso de Empate
    if escolha_usuario == escolha_computador:
        print("Empate!")
        empates += 1
        
    # Caso de Vitória do Usuário
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        
        print("🎉 VOCÊ VENCEU A RODADA! 🎉")
        vitorias_usuario += 1
        
    # Caso de Vitória do Computador (tudo que não é empate nem vitória do usuário)
    else:
        print("🤖 O computador venceu a rodada.")
        vitorias_computador += 1

# --- Fim do Jogo ---
print("\n==================================")
print(f"FIM DO JOGO! Você alcançou {vitorias_usuario} vitórias.")
print(f"PLACAR FINAL: Você {vitorias_usuario} x {vitorias_computador} Computador (Empates: {empates})")
print("PARABÉNS PELA VITÓRIA!")
print("==================================")
# %%