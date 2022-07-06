class Bank:
    def __init__(self):
        self.__bank_data = {}

    # add an entry with the card number and pin number
    def add_entry(self, card_num: int, pin: int) -> None:
        self.__bank_data[card_num] = {"account": {}, "pin": pin}

    # add an account with account name and amount
    def add_account(self, card_num: int, account: str, amount: int) -> None:
        if card_num in self.__bank_data:
            self.__bank_data[card_num]["account"][account] = amount

    # update an account with new amount(balance)
    def update_account(self, card_num: int, account: str, amount: int) -> bool:
        if (
                self.__bank_data[card_num]["account"][account]
                in self.__bank_data[card_num]["account"]
        ):
            self.__bank_data[card_num]["account"] = amount
            return True
        else:
            return False

    # check the entered account and pin number,
    # and returns the account information if the pin number is correct
    def check_pin(self, card_num: int, input_pin: int) -> dict or None:
        if (
                card_num in self.__bank_data
                and self.__bank_data[card_num]["pin"] == input_pin
        ):
            return self.__bank_data[card_num]["account"]
        else:
            return None


class AtmController:
    def __init__(self, bank: Bank, cash_bin: int):
        self.bank = bank
        self.accounts = None
        self.cash_bin = cash_bin

    # Use the Bank class's check_pin method to check the pin number and return the result
    def get_account(self, card_num: int, pin: int) -> None or dict:
        self.accounts = self.bank.check_pin(card_num, pin)
        if self.accounts is None:
            return self.accounts
        else:
            return self.accounts

    # Verify that the selected account existed and return the result
    def select_account(self, account: str) -> bool:
        if account in self.accounts:
            return True
        else:
            return False

    # Returns the balance of the account entered
    def get_balance(self, account: str) -> (bool, int):
        return True, self.accounts[account]

    # After despositing the amount entered into specified account, update the bank's account
    def desposit(self, card_num: int, account: str, amount: int) -> (bool, int):
        self.cash_bin += amount
        self.accounts[account] += amount
        self.bank.update_account(card_num, account, self.accounts[account])
        return True, self.accounts[account]

    # After withdrawing the amount entered from the specified account, update the bank's acount
    # This will not be done if the ATM is short of remaining cash
    def withdraw(self, card_num: int, account: str, amount: int) -> (bool, int):
        if self.accounts[account] >= amount and self.cash_bin >= amount:
            self.accounts[account] -= amount
            self.bank.update_account(card_num, account, self.accounts[account])
            return True, self.accounts[account]
        else:
            return False, self.accounts[account]

    # Executes the method according to the action entered
    def run_actions(
            self, card_num: int, account: str, action: str, amount: int
    ) -> (bool, int) or bool:
        if action == "see balance":
            return self.get_balance(account)
        elif action == "desposit":
            return self.desposit(card_num, account, amount)
        elif action == "withdraw":
            return self.withdraw(card_num, account, amount)
        else:
            return False, None

    # Runs the operation flow of the ATM on call
    def __call__(
            self, card_num: int, pin: int, account: str, action: str, amount: int = 0
    ):
        print(
            f"[{card_num} | {account}] {action} {amount}"
            if action != "see balance"
            else f"[{card_num} | {account}] {action}"
        )
        accounts = self.get_account(card_num, pin)
        if accounts is None:
            print("Invalid card or Incorrect pin\n")
            return
        if not self.select_account(account):
            print("Invalid account\n")
            return
        status, balance = self.run_actions(card_num, account, action, amount)
        if status:
            print(f"Balance: {balance}$\n")
            return
        else:
            print(f"Invalid action\n")
            return


def main():
    test_bank = Bank()
    test_bank.add_entry(123456789, 1234)
    test_bank.add_account(123456789, "account_a", 1000)
    test_bank.add_account(123456789, "account_b", 2000)

    test_bank.add_entry(987654321, 4321)
    test_bank.add_account(987654321, "account_c", 3000)
    test_bank.add_account(987654321, "account_d", 4000)

    test_atm = AtmController(test_bank, 1000)
    test_atm(123456789, 1234, "account_a", "see balance")
    test_atm(123456789, 1234, "account_a", "withdraw", 100)
    test_atm(123456789, 1234, "account_a", "desposit", 100)
    test_atm(123456789, 1234, "account_a", "see balance")
    test_atm(123456780, 1234, "account_a", "see balance")  # Invalid card or Incorrect pin (input wrong card number)
    test_atm(123456789, 1235, "account_a", "see balance")  # Invalid card or Incorrect pin (input wrong pin number)
    test_atm(123456789, 1234, "account_a", "withdraw", 1100)  # Invalid Action (withdraw more than the ATM has)
    test_atm(123456789, 1234, "account_c", "see balance")  # Invalid account (input non exist account)
    test_atm(123456789, 1234, "account_a", "wrong action")  # Invalid action (input wrong action)

    test_atm(123456789, 1234, "account_b", "see balance")
    test_atm(123456789, 1234, "account_b", "desposit", 3000)
    test_atm(123456789, 1234, "account_b", "withdraw", 99999)  # Invalid card or Incorrect pin (input wrong pin number)
    test_atm(123456789, 1234, "account_b", "see balance")

    test_atm(987654321, 4321, "account_c", "see balance")
    test_atm(987654321, 1234, "account_c", "see balance")  # Invalid card or Incorrect pin (input wrong pin number)

    test_atm(99999999, 1323, "account_a", "see balance")  # Invalid card or Incorrect pin (input wrong card number)

    """
    Add test cases here
    Ex) test_atm(123456789, 1234, "account_a", "see balance")
    """


if __name__ == "__main__":
    main()
