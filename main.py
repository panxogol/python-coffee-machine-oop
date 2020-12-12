from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def start(menu=Menu(), coffee_maker=CoffeeMaker(), money_machine=MoneyMachine()):
    # TODO 1: Prompt user asking what would you like?
    answer_list = ["espresso", "latte", "cappuccino", "off", "report"]
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while answer not in answer_list:
        print("Wrong answer. Please type again.")
        answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO 2: Turn off the coffee machine by entering off to the prompt
    if answer == "off":
        print("Turning off the coffee machine. Good bye.")
        return

    # TODO 3: Print Report
    elif answer == "report":
        coffee_maker.report()

    # TODO 4: Check resources suficient
    elif menu.find_drink(answer) is not None:
        item = menu.find_drink(answer)
        if coffee_maker.is_resource_sufficient(item):

            # TODO 5: Process coins
            payment_successfully = money_machine.make_payment(item.cost)

            # TODO 6: Check transaction successfull?
            if payment_successfully:
                # TODO 7: Make coffee
                coffee_maker.make_coffee(item)

    # Restart
    start(menu, coffee_maker, money_machine)


# Make the program work
start()
