# Python Bank
# use of methods
# The user needs to be able to make a deposit
# The user needs to be able to pull money out
# The user needs to be able to pay a bill
# The program needs to track the money in the bank
# The user needs to be able to look up their balance
# The program needs to keep running until the user decides to quit the program.


balance = 100

def withdrawal():
    global balance
    print("How much would you like to withdraw? ")
    withdrawal_amount = float(input("The amount? "))
    balance -= withdrawal_amount
    withdrawal_result = str(balance)
    print("Your remaining balance will be..." + withdrawal_result)

def deposit():
    global balance
    print("Fantastic, how much are you depositing today")
    deposit_amount = float(input("How much would you like to deposit? "))
    balance += deposit_amount
    deposit_result = str(balance)
    print("Your balance is now..." + deposit_result)

def bill_pay():
    global balance
    print("What is the amount of the bill? ")
    payment_amount = float(input("Payment amount? "))
    balance -= payment_amount
    payment_result = str(balance)
    payee = input("Whom shall we make this out to? ")
    print("Ok, your remaining balance will be " + payment_result + "And we made the payment to " + payee)

def check_balance():
    global balance
    balance_reconfig = str(balance)
    print("Your balance is " + balance_reconfig)

def greeting():
    print("What type of transaction can we help you with today deposit, withdrawal, check your balance, or are you paying a bill? ")

def farewell():
    print("Thank you for visiting PyBank today. Have a nice day.")

print("Welcome to PyBank International. ")

engaged = True

while engaged:

    greeting()

    answer = input("Type of transaction: ")
    if answer == 'withdrawal':
        withdrawal()    

    elif answer == 'deposit':
        deposit()    

    elif answer == 'paying a bill':
        bill_pay()

    elif answer == 'check my balance':
        check_balance()

    else:
        print("I'm sorry, we are only a bank. ")
        greeting()

    x = input("Can I help you with anything else today?")

    if x == 'yes':
        continue

    else:
        farewell()
        break

