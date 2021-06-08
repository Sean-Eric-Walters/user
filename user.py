class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def dispaly_user_balance(self):
        print(self.name, self.account_balance)

    def tranfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Batou = user('Batou', 'Batou@section9.gov' )
Togusa = user('Togusa', 'Togusa@section9.gov')
Major = user('Major', 'Major@section9.gov')

print('==balance==')

Batou.make_deposit(4999)
Batou.make_deposit(4999)
Batou.make_deposit(1698.58)
Batou.make_withdrawal(2800)
Batou.dispaly_user_balance()

Togusa.make_deposit(1589.31)
Togusa.make_withdrawal(243.19)
Togusa.make_deposit(1589.31)
Togusa.make_withdrawal(2000)
Togusa.dispaly_user_balance()

Major.make_deposit(9000)
Major.make_withdrawal(1100)
Major.make_withdrawal(89.13)
Major.make_withdrawal(983.21)
Major.dispaly_user_balance()

print('==balance==')

Batou.tranfer_money(Major,3000)
Batou.dispaly_user_balance()
Major.dispaly_user_balance()