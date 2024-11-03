from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

condition = True
while condition:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        condition = False
        print("Goodbye!")

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    elif choice == "cappuccino" or choice == "latte" or choice == "espresso":
        drink = menu.find_drink(choice)
        sufficient = coffee_maker.is_resource_sufficient(drink)
        if sufficient:
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)
    else:
        print("Sorry you typed wrong input, try again...")