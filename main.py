import coffee_maker
import menu
from turtle import clear
from coffee_maker import CoffeeMaker


latte = menu.Menu()
resource_sufficient = CoffeeMaker()
report = coffee_maker.CoffeeMaker()
output = menu.Menu()
choice = input(f"Which coffee do you want? ({output.get_items()}) ")

print(latte.menu())
if choice == "off":
    clear()
    exit()
elif choice == "report":
    print(report.report())

resource_sufficient.is_resource_sufficient(choice)
