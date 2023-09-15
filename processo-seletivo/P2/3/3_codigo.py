def calcula_troco(valor):
    total = valor

    notas_100 = int(total // 100)
    total %= 100

    notas_50 = int(total // 50)
    total %= 50

    notas_20 = int(total // 20)
    total %= 20

    notas_10 = int(total // 10)
    total %= 10

    notas_5 = int(total // 5)
    total %= 5

    notas_2 = int(total // 2)
    total %= 2

    moedas_1 = int(total // 1)
    total %= 1

    moedas_50 = int(total // 0.5)
    total %= 0.5

    moedas_25 = int(total // 0.25)
    total %= 0.25

    moedas_10 = int(total // 0.10)
    total %= 0.10

    moedas_5 = int(total // 0.05)
    total %= 0.05

    moedas_1_centavo = int(total * 100)

    print("NOTAS:")
    print(f"{notas_100} nota(s) de R$ 100.00")
    print(f"{notas_50} nota(s) de R$ 50.00")
    print(f"{notas_20} nota(s) de R$ 20.00")
    print(f"{notas_10} nota(s) de R$ 10.00")
    print(f"{notas_5} nota(s) de R$ 5.00")
    print(f"{notas_2} nota(s) de R$ 2.00")

    print("\nMOEDAS:")
    print(f"{moedas_1} moeda(s) de R$ 1.00")
    print(f"{moedas_50} moeda(s) de R$ 0.50")
    print(f"{moedas_25} moeda(s) de R$ 0.25")
    print(f"{moedas_10} moeda(s) de R$ 0.10")
    print(f"{moedas_5} moeda(s) de R$ 0.05")
    print(f"{moedas_1_centavo} moeda(s) de R$ 0.01")


def main():
    valor = input()

    if valor.replace('.', '').isdigit() and valor.count('.') == 1:
        valor = float(valor)
        if valor < 0:
            print("Input inválido")
        else:
            calcula_troco(valor)
    else:
        print("Input inválido")


if __name__ == "__main__":
    main()
