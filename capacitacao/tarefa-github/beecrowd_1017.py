tempo_gasto = float(input())
velocidade_maxima = float(input())

distancia = tempo_gasto * velocidade_maxima

quantidade_litros_necessarios = distancia / 12

print(f"{quantidade_litros_necessarios:.3f}")
