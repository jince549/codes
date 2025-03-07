
def show_menu(lst):
    for i, j in enumerate(lst):
        print(i+1, j)

def set_budget():
    global initial_budget
    initial_budget = float(input("Please enter your initial Budget :"))
    return initial_budget

def add_expense_details(details):
    def discription():
        discription_items =  input("Please enter the discreption :")
        return discription_items

    def add_expense():   
        expense_amount = float(input("Please enter the expense amount :"))
        return expense_amount
    details[discription()] = add_expense()

def show_details(detail_dict):
    print("Total Budget is :", initial_budget)
    print("Expences are")
    print("____________________________")
    for i, j in detail_dict.items():
        print(f"{i} - {j}")
    print("____________________________")
    total_spend = sum(detail_dict.values())
    print(f"Total spend : {total_spend}")
    balance = initial_budget - total_spend
    print(f"Balance amount : {balance}")



print("Welcome Budget Tracking app")
expense_details = {}
initial_budget = 0
menu_list = ["Set Budget", "Add Expense", "Show Budget Details", "Exit"]
show_menu(menu_list)
while True:
    try:
        user_input = int(input("Please choose an option(1/2/3/4) :"))
    except ValueError:
        print("Please enter a valid input")
    else:
        if user_input == 1:
            set_budget()
            print("Budget added sucessfully")

        elif user_input == 2:
            if initial_budget == 0:
                print("Budget amount is 0: Please add budget")
                
            else:
                add_expense_details(expense_details)
                print("Expense added sucessfully")
            
        elif user_input == 3:
            show_details(expense_details)

        elif user_input == 4:
            print("Thank you")
            break
        else:
            print("Invalid input")
