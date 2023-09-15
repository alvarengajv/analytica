def movimentacao_cavalo(posicao_inicial, posicao_final):
    movimentos_validos = [
        (-2, -1), (-2, 1), (-1, -2), (-1, 2),
        (1, -2), (1, 2), (2, -1), (2, 1)
    ]

    return posicao_final in [(posicao_inicial[0] + dx, posicao_inicial[1] + dy) for dx, dy in movimentos_validos]


def main():
    while True:
        movimento = input()
        if movimento == "f":
            print("Fim...")
            break

        posicoes = movimento.split()
        if len(posicoes) != 2:
            print("Input inválido")
            continue

        posicao_inicial, posicao_final = posicoes

        if len(posicao_inicial) != 2 or len(posicao_final) != 2:
            print("Input inválido")
            continue

        if not (posicao_inicial[0].isalpha() and posicao_final[0].isalpha()):
            print("Input inválido")
            continue

        if not (posicao_inicial[1].isdigit() and posicao_final[1].isdigit()):
            print("Input inválido")
            continue

        letra_inicial, numero_inicial = ord(posicao_inicial[0].lower()) - ord('a'), int(posicao_inicial[1]) - 1
        letra_final, numero_final = ord(posicao_final[0].lower()) - ord('a'), int(posicao_final[1]) - 1

        posicao_inicial = (letra_inicial, numero_inicial)
        posicao_final = (letra_final, numero_final)

        if movimentacao_cavalo(posicao_inicial, posicao_final):
            print("VÁLIDO")
        else:
            print("INVÁLIDO")


if __name__ == "__main__":
    main()
