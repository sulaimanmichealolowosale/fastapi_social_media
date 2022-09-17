from app.calculations import *
import pytest



@pytest.fixture
def zero_bank_account():
    print("Creating a zero bank account")
    return BankAccount()


@pytest.fixture
def bank_account():
    print("Initializing bank account")
    return BankAccount(50)




# def test_add():
#     sum=add(2,8)
#     assert sum ==10


# def test_subtract():
#     assert subtract(10, 5)==5

# def test_divide():
#     assert divide(10, 5)==2

# def test_multiply():
#     assert multiply(10, 5)==50



def test_bank_account_default_balance(zero_bank_account):
    assert zero_bank_account.balance == 0



@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (1200, 500, 700),
    (50, 10, 40)
    ])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)

    assert zero_bank_account.balance == expected