"""Ask the numbers with which we are going to operate."""
while True:
    from time import sleep

    ask = input('\nHello! Are you here for calculating?(y/n) ')
    if ask == 'y':
        print('OK! LOADING...')
        sleep(2)
    elif ask == 'n':
        quit()

    print('\nEnter two numbers\n\
    (one number, press enter and second number, press enter)')
    num1 = int(input(" "))
    num2 = int(input(" "))


    def sumar(num1: int, num2: int):
        """Sum num1 and num2."""
        var_sum = num1 + num2
        return var_sum


    def restar(num1: int, num2: int):
        """Subtract num1 and num2."""
        var_sub = num1 - num2
        return var_sub


    def multiplicar(num1: int, num2: int):
        """Multiply num1 and num2."""
        var_mul = num1 * num2
        return var_mul


    def dividir(num1: int, num2: int):
        """Divide num1 and num2."""
        var_div = num1 / num2
        return var_div


    calc = input('Seleciona la operación que quieras realizar\n\
        + = Suma\n\
        - = Resta\n\
        * = Multiplicación\n\
        / = División\n\
        presiona "q" si quieres salir ')

    if calc == 'q':
        exit()
    elif calc == "+":
        print(f"Este es el resultado de tu operación: {sumar(num1, num2)}")
    elif calc == "-":
        print(f"Este es el resultado de tu operación: {restar(num1, num2)}")
    elif calc == "*":
        print(f"Este es el resultado de tu operación: {multiplicar(num1, num2)}")
    elif calc == "/":
        if num2 != 0:
            print(f"Este es el resultado de tu operación: {dividir(num1, num2)}")
    else:
        print("Por favor, escribe un operador")



