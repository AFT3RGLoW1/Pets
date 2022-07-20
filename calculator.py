from colorama import init
from colorama import Fore, Back

while True:
    init()
    print(Fore.BLACK)
    print(f"{Back.RED}Zero will terminate session")
    what = input(f"{Back.GREEN}What we're gonna do? (+, -, *, /): ")
    if what == '0':
        break
    try:
        a = float(input(f"{Back.CYAN}First number: "))
        b = float(input(f"{Back.CYAN}Second number: "))
    except ValueError:
        print(f"{Back.RED}Please use numbers!")
        continue

    if what == "+":
        c = a + b
        print(f"{Back.YELLOW}Result: " + str(c))

    elif what == "-":
        c = a - b
        print(f"{Back.YELLOW}Result: " + str(c))

    elif what == "*":
        c = a * b 
        print(f"{Back.YELLOW}Result: " + str(c))

    elif what == "/":
        if b != 0:
            c = a / b 
            print(f"{Back.YELLOW}Result: " + str(c))
        else:
            print(f"{Back.RED}Error!!!")

    else:
        print(f"{Back.RED}Error!")
    input()
