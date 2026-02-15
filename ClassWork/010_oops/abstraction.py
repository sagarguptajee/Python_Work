from abc import ABC , abstractmethod


class Account(ABC):
    balance=0

    @abstractmethod  #method without implimantation
    def deposite(self,amt):
         pass
    
    @abstractmethod
    def withdrow(self,amt):
         pass
    
    def checkbalance(self):
         print(f"current balance is {self.balance}")



class SavingAccount(Account):
     
     def deposite(self, amt):
          self.balance=self.balance+amt
    

     def withdrow(self, amt):
            if amt>self.balance:
               print("insuficiant balance")

            else:
                 self.balance-=amt


# s=SavingAccount()

# s.checkbalance()
# s.deposite(5000)
# s.withdrow(1000)
# s.checkbalance()



class LoanAccount(Account):
     
    def deposite(self, amt):
            if amt>self.balance:
               print("loan amount is greater than you paying")
            else:
                 self.balance-=amt
    def withdrow(self, amt):
         self.balance+=amt


l=LoanAccount()
l.withdrow(50000)
l.checkbalance()
l.deposite(9000)
l.checkbalance()
l.deposite(42000)
l.checkbalance()
l.deposite(41000)
l.checkbalance()

    

