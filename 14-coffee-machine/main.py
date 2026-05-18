import menu_list



def report(money_right_now):
    print(f'Water: {menu_list.resources["water"]}ml')
    print(f'Milk: {menu_list.resources["milk"]}ml')
    print(f'Coffee: {menu_list.resources["coffee"]}g')
    print(f'Money: ${money_right_now}')

def materials_enough(choice):
    if menu_list.resources["water"] - menu_list.Menu[choice]["ingredients"]["water"] >= 0 and menu_list.resources["coffee"] - menu_list.Menu[choice]["ingredients"]["coffee"] >= 0:
        if choice == "espresso":
            return [True]
        else:
            if menu_list.resources["milk"] - menu_list.Menu[choice]["ingredients"]["milk"] >=0:
                return [True]
            else:
                return [False,"milk"]
    else:
        if menu_list.resources["water"] - menu_list.Menu[choice]["ingredients"]["water"] < 0:
            return [False,"water"]
        else:
            return [False,"coffee"]
def money_check(price):
    try:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        money_offered = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
        if money_offered > price:
            change = round(money_offered - price,2)
            print(f"Here is ${change} in change.")
            return True
        elif money_offered == price:
            print(f"No change. You gave me the money just right")
            return True
        else:
            print("Sorry that's not enough money.Money refunded.")
            return False
    except ValueError:
        print("Invalid Money offered")

def order(choice):
    money_needed  = menu_list.Menu[choice]["cost"]/10
    if money_check(money_needed):
        menu_list.resources["money"] += money_needed
        menu_list.resources["water"] -= menu_list.Menu[choice]["ingredients"]["water"]
        menu_list.resources["coffee"] -= menu_list.Menu[choice]["ingredients"]["coffee"]
        if choice != "espresso":
            menu_list.resources["milk"] -= menu_list.Menu[choice]["ingredients"]["milk"]
        print(f"Here is your {choice} ☕. Enjoy!")



while True:
    money = menu_list.resources["money"]
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "report":
        report(money)
    elif customer_choice == "espresso" or customer_choice == "latte" or customer_choice == "cappuccino":
        sufficient = materials_enough(customer_choice)
        if sufficient[0]:
            order(customer_choice)
        else:
            print(f"Sorry there is not enough {sufficient[1]}.")
    elif customer_choice == "off":
        print("Machine is under maintenance")
        break
    else:
        print("Invalid order,check the menu better!!")
    if menu_list.resources["water"] < 50 or menu_list.resources["coffee"] < 18:
        print("Machine cant make any more coffee until more resources are given!!")
        break
