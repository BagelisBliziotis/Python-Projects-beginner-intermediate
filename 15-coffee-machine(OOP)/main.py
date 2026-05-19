from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee = CoffeeMaker()
my_moneyMachine = MoneyMachine()

while True:
    choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if choice == "latte" or choice == "cappuccino" or choice == "espresso":
        order = my_menu.find_drink(choice)
        if order is None:
            print("Sorry, check the menu again!")
        else:
            if my_coffee.is_resource_sufficient(order):
                if my_moneyMachine.make_payment(order.cost):
                    my_coffee.make_coffee(order)
    elif choice == "report":
        my_coffee.report()
        my_moneyMachine.report()
    elif choice == "off":
        print("Machine is under maintenance")
        break
    else:
        print("Invalid Input")

