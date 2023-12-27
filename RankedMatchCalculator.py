# #%%

# Instruções para entrega
#  # 2️⃣ Calculadora de partidas Rankeadas
# **O Que deve ser utilizado**

# - Variáveis
# - Operadores
# - Laços de repetição
# - Estruturas de decisões
# - Funções

# ## Objetivo:

# Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
# depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

# Se vitórias for menor do que 10 = Ferro
# Se vitórias for entre 11 e 20 = Bronze
# Se vitórias for entre 21 e 50 = Prata
# Se vitórias for entre 51 e 80 = Ouro
# Se vitórias for entre 81 e 90 = Diamante
# Se vitórias for entre 91 e 100= Lendário
# Se vitórias for maior ou igual a 101 = Imortal

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**"

#%%

#1 function
def test(match):

    if match <= 10:
        rank = "Iron"
        return rank
    
    elif 11 <= match <=20:
        rank = "Bronze"
        return rank 
    
    elif 21 <= match <= 50:
        rank = "Silver"
        return rank
    
    elif 51 <= match <=80:
        rank = "Gold"
        return rank
    
    elif 81 <= match <=90:
        rank = "Diamond"
        return rank
    
    elif 91 <= match <=100:
        rank = "Legendary"
        return rank
    
    elif match > 100:
        rank = "Imortal"
        return rank


#2 input
try:
    victory = int(input("Please write how many matches you've won:\n"))
except ValueError:
        print("Don't try to cheat, we need your battle numbers, warrior!")
        raise SystemExit()

   

try:
    lost = int(input("Please write how many matches you've lost:\n"))
except ValueError:
    print("You gotta face the truth to become a better warrior! Tell me your defeat numbers!")
    raise SystemExit()

match = (victory-lost)


#3 output

result = test(match)
print(f"The Warrior has a balance of {match} and is at the {result} rank!")


#