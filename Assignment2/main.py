import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    ###  write the rest of the codes ###
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large/off): ")
        
        if choice == "off":
            is_on = False
        
        elif choice in recipes:
            sandwich = recipes[choice]
            cost = sandwich["cost"]

            if SandwichMaker.check_resources(sandwich):
                payment = cashier_instance.process_coins()

                if cashier_instance.transaction_result(payment,cost):
                    sandwich_maker_instance.make_sandwich(choice,sandwich)
if __name__=="__main__":
    main()
