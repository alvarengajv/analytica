def calcula_angulo(horario):
    horas, minutos = map(int, horario.split(':'))

    if len(horario) != 5:
        print("Input inválido")
        return None

    if horas < 0 or minutos < 0 or horas > 23 or minutos > 59:
        print("Input inválido")
        return None

    horas %= 12

    angulo_minutos = (360 / 60) * minutos
    angulo_horas = (360 / 12) * horas

    angulo_ponteiros = abs(angulo_horas - angulo_minutos)

    menor_angulo_ponteiros = min(360 - angulo_ponteiros, angulo_ponteiros)

    return menor_angulo_ponteiros


def main():
    while True:
        horario = input()
        if horario == 'f':
            print("Fim...")
            break

        else:
            angulo = calcula_angulo(horario)
            if angulo is not None:
                print(f"O menor ângulo é de {angulo:.0f}°")

            else:
                continue


if __name__ == "__main__":
    main()
