class User:
    def __init__(self, name, age, gender):
        self.name= name
        self.age=age
        self.gender = gender
    def show_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender} ")
    def show_name(self):
        print(f"\nAccount Holder: {self.name}\n")
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance= 0
    def deposit(self,ammount):
        self.ammount= ammount
        self.balance= self.ammount+self.balance
        print(f"{self.ammount}$ has been added to you balance your new balance is {self.balance}$")
    def withdraw(self, ammount):
        self.ammount= ammount
        if self.ammount> self.balance:
            print('not enough funds')
        else:
            self.balance = self.balance - self.ammount
            print(f"{self.ammount}$ has been withdrawn, you have {self.balance}$ left in your account")
    def show_balance(self):
        print(f"\n{self.name}'s balance: {self.balance}$\n")
    def transactions(self):
        transaction=[]
        pass






# Pablo= Bank('Pablo', 18,'M')
# User.show_info(Pablo)

# Bank.show_balance(Pablo)
# while True:
#     Bank.deposit(Pablo, int(input("how much do you want to deposit")))
#     Bank.show_balance(Pablo)

while True:
    member=input("do you have an account already: Y or N").upper()
    if member== 'N':
        member1=Bank(input("whats your name"), int(input('whats your age')),input("whats your gender"))
    else:
        pass
    leave= False
    while leave!=True:
        Bank.show_name(member1)
        decision=input('\nDo you want to \n1:deposit money \n2: Withdraw money\n3: Chack balance\n4: leave')
        if decision== '1':
            d_ammount= int(input("how much do you want to deposit"))
            Bank.deposit(member1,d_ammount)
        elif decision=='2':
            w_ammount=int(input("how much do you want to withdraw"))
            Bank.withdraw(member1,w_ammount)
        elif decision== '3':
            Bank.show_balance(member1)
        elif decision== '4':
            leave= True