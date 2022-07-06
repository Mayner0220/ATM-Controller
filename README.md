# ATM-Controller
### Environment
- Python >= 3.8

### How to run code
```
# run command
python atm_controller.py
```

### How to add test case
Follow the class and method usage below to add the case you want to test the main funtion in the code.

- Bank
  - Bank()
    ```
    dummy_bank = Bank()
    ```
  - Bank.add_entry()
    ```
    dummy_bank.add_entry(card_num, pin)
    Ex) dummy_bank(123456789, 1234)
    ```
  - Bank.add_account()
    ```
    dummy_bank.add_account(card_num, account, amount)
    Ex) dummy_bank.add_account(123456789, "dummy_account", 100)
    ```
- AtmController
  - AtmController()
    ```
    dummy_atm = AtmController(Bank, cash_bin)
    Ex) dummy_atm = AtmController(dummy_bank, 1000)
    ```
  - AtmController.__call__()
    ```
    dummy_atm(card_num, pin, account, action, amount)
    
    Ex) See balance
    dummy_atm(123456789, 1234, "dummy_account", "see balance")
    
    Ex) Desposit
    dummy_atm(123456789, 1234, "dummy_account", "desposit", 100)
    
    Ex) Withdraw
    dummy_atm(123456789, 1234, "dummy_account", "withdraw", 100)
    ```