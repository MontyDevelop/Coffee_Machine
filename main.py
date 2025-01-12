from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Now do not touch or open any of the other file and you have to identify all methods here
# You have to trust these file like package you have used before

# Use document to solve the problems

# file:///C:/Users/Monty/Downloads/Coffee+Machine+Classes+Documentation.pdf
# file:///C:/Users/Monty/Downloads/Coffee+Machine+Program+Requirements.pdf


money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()

is_on = True

# money_machine.report()
# coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would u like? ({options}) ")
    if choice == 'off':
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        # print(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

