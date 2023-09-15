def frequencia_numeros():
    numeros = {}
    while True:
        entrada = input()
        if entrada == 'f':
            break

        if entrada.isdigit():
            numero = int(entrada)
            if numero in numeros:
                numeros[numero] += 1
            else:
                numeros[numero] = 1

    for numero, frequencia in numeros.items():
        if frequencia == 1:
            print(f"O número {numero} apareceu 1 vez")
        else:
            print(f"O número {numero} apareceu {frequencia} vezes")

    print("Fim...")


def main():
    frequencia_numeros()


if __name__ == "__main__":
    main()
