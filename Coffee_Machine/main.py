from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items()
    coffee = input(f"What would you like? {options}")
    if coffee == "off":
        is_on = False
    elif coffee == "report":
        print(coffee_maker.report())
        print(money.report())
    else:
        drink = menu.find_drink(coffee)
        print(drink)

