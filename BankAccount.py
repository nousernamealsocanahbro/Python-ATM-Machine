from Validator import validate_input

class BankAccount:
    def __init__(self, first_name: str, last_name: str, balance: float, pin: int):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = balance
        self.pin = pin

    def show_details(self):
        print(f"First name: {self.first_name}\nLast name: {self.last_name}\nBalance: ${self.balance:.2f}")

    def deposit(self):
        deposit_amount = validate_input("Input deposit amount: ", float, lambda x: x > 0, "Amount cannot be a negative number.")

        self.balance += deposit_amount

        print(f"You have deposited ${deposit_amount:.2f}")
        print(f"Balance: ${self.balance:.2f}")

    def withdraw(self):
        withdraw_amount = validate_input("Input withdraw amount: ", float, lambda x: 0 < x <= self.balance, "Cannot withdraw more than amount in balance.")

        self.balance -= withdraw_amount

        print(f"You have withdrawn ${withdraw_amount:.2f}")
        print(f"Balance: ${self.balance:.2f}")

    def login(self):
        is_pin_valid = False
        tries = 3

        while not is_pin_valid and tries > 0:
            try:
                pin = int(input("Input your pin: "))

                if pin != self.pin:
                    print("Wrong pin, please try again.\n")
                    tries -= 1
                else:
                    is_pin_valid = True
            except ValueError as e:
                print(f"{e}, please try again.\n")

        if tries == 0:
            print("Too many invalid pins. Your account has been locked.")
            exit()