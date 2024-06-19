from bank_account import *

Riyaz=Bankaccount(1000,"Riyaz")
Shoaib=Bankaccount(2000,"Shoaib")


Riyaz.getBalance()
Shoaib.getBalance()
Riyaz.deposit(200)

Riyaz.withdraw(10000)
Riyaz.withdraw(14)

Riyaz.transfer(10000,Shoaib)
Riyaz.transfer(51,Shoaib)

Mohammed=IntrestRewardsAcct(1500,"Mohammed")
Mohammed.getBalance()
Mohammed.deposit(100)
Mohammed.transfer(100,Riyaz)

Raghav = SavingsAcct(1000, "Raghav")
 
Raghav.getBalance()

 
Raghav.deposit(100)
 
Raghav.transfer(10000, Riyaz)
Raghav.transfer(100, Riyaz)