
def create_account(name, account_number, balance=0):
    return {
        "name": name,
        "account_number": account_number,
        "balance": balance
    }

def get_balance(account):
    return account["balance"]
