"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import re

from pandas import notnull

class Employee:
    def __init__(self, name, contractType, salary, hours, ):
        self.contractType = contractType
        self.name = name
        self.salary = salary
        if contractType=="hourly":
            self.hours = hours
        self.bonus = None
        self.commissionType = None
        self.output = ""
        if contractType == "monthly":
            self.output += (name + " works on a " + contractType + " salary of " + salary)
        elif contractType == "hourly":
            self.output += (name + " works on a contract of " + hours + " at " + salary + "/ hour")


    def bonus_calc(self, commissionType, commissionPay, contracts):
        if commissionType=="contract":
            self.commissionType = commissionType
            self.bonus = commissionPay * contracts
            self.output+= (" and recieves a commission for " + contracts + " contract(s) at " + commissionPay + "/contract")
        else:
            self.bonus = commissionPay
            self.output+= (" and recieves a bonus commission of " + commissionPay)

    def get_pay(self):
        if self.contractType == "hourly":
            pay = self.hours * self.salary
        else: 
            pay = self.salary
        if self.bonus != None:
            pay += self.bonus
        self.pay = pay
        

    def __str__(self):
        self.get_pay(self)
        self.output(". Their total pay is " + self.pay +".")

        

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", 4000, None)
billie.__str__()

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 25, 100)
charlie.__str__()

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", 3000, None)
renee.bonus_calc("contract", 200, 4)
renee.__str__()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 25, 150)
jan.bonus_calc("contract", 220, 3)
jan.__str__()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", 2000, None)
robbie.bonus_calc("bonus", 1500, None)
robbie.__str__()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 30, 120)
ariel.bonus_calc("bonus", 600, None) 
ariel.__str__()