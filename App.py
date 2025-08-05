from BankAccount import BankAccount
from Validator import validate_input
        
def main():
    print("Before you can use our bank app, you will need to make an account")
    first_name = input("Input first name: ").capitalize().strip()
    last_name = input("Input last name: ").capitalize().strip()
    pin = validate_input("Input PIN: ", int, lambda x: len(str(x)) == 4, "PIN must be 4 digits long")
    myAccount = BankAccount(first_name, last_name, 0, pin)

    print("\nNow we will need you to login")
    myAccount.login()
    while True:
        print("What would you like to do? (1-4)")
        print("1. View details")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")

        action = validate_input("> ", int, lambda x: 0 < x <= 4, "Invalid input")

        match action:
                case 1:
                    myAccount.show_details()
                case 2:
                    myAccount.deposit()
                case 3:
                    myAccount.withdraw()
                case 4:
                    print("Logging out")
                    exit()
        input() # give user time to read output

if __name__ == "__main__":
    main()