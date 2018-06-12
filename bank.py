class Customer:
	def __init__(self, name, accountno, address, balance):
		self.name = name
		self.accountno = accountno
		self.address = address
		self.balance = balance
	def displayCustomer(self):
		print "name : ",self.name,"accountno : ",self.accountno,"address : ", self.address,"balance : ",self.balance
cust=Customer("aaa",123456789,2333,56789)
cust1=Customer("bbb",987654321,1234,9000)
cust.displayCustomer()		
cust1.displayCustomer()
