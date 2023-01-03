def calcule(num1, operator, num2):
    match operator:
        case "+":
            return (num1 + num2)
        case "-":
            return (num1 - num2)
        case "*":
            return (num1 * num2)
        case "/":
            return (num1 / num2)
        case "%":
            return (num1 % num2)
        case _:
            print("operateur invalide")
            return (0)

print(calcule(75 ,"%" ,12))
print(calcule(75 ,"+" ,12))
print(calcule(75 ,"*" ,12))