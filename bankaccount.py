class BankAccount :
    def __init__(self,account_holder: str, initial_balance: float = 0.0):
        self.accout_holder = account_holder
        self._balance = initial_balance
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, amount:float) -> None:
        if amount < 0:
            raise ValueError("余额不能为负数")
        self._balance = amount

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("存款金额须>0")
        self.balance += amount
        
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("取款金额必须>0")
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
    
    def __repr__(self) -> str:
        return f"BankAccount(holder={self.accout_holder},balance={self.balance})"
    

#测试
if __name__ == "__main__":
    account = BankAccount("zhu" , 10.0)
    print(account)

    account.deposit(10.0)
    print("存款后余额：" , account.balance)

    account.withdraw(5.0)
    print("取款后余额：" , account.balance)

    try:
        account.withdraw(30)
    except ValueError as e:
        print(e) #余额不足

    try:
        account.withdraw(-30)
    except ValueError as e:
        print(e) #取款＞0
