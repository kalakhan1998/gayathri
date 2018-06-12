def verify_pin(pin):
    if pin == 1998:
	return True
    else:
	return False
def log_in():
    tries = 0
    while tries < 2:
	pin = int(input("enter a no"))
	if verify_pin(pin):
	    print("pin is correct")
            print("tq")
	    return True
	else:
	    print("pin is incorrect")
	    tries += 1
    print("ur card vil be block")
    return False

def start_menu():
    print("welcome to atm")
    if log_in():
   	 print("exiting program")
start_menu()



