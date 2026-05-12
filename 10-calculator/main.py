import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators =  {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
result = 0
check = True
while True:
    if check:
        print(art.logo)
        first_number = float(input("What's the first number?: "))
    else:
        first_number = result
    print("+")
    print("-")
    print("*")
    print("/")
    operator = input("Pick an operator: ")
    second_number = float(input("What's the next number?: "))
    result = operators[operator](first_number,second_number)
    print(f"{first_number} {operator} {second_number} = {result}")
    question = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculation: ")
    if question != "y":
        print("\n"*100)
        check = True
    else:
        check = False
