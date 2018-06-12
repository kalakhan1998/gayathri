print("welcome to atm")
pin = 123
balance=100000
a=int(input("enter ur pin"))
if pin == a:
	print("pin is correct")
	b=int(input("enter amount"))
	balance=balance-b
	print(balance)
else:
	print("incorrect pin")
if b > balance:
	print("insufficient money")
else:
	print(balance)


