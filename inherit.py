class Parent:
ParentAttr = 100
	def __init__(self):
		print "calling parent constructor"
	def ParentMethod(self):
		print "calling parent method"
	def setAttr(self,attr):
		Parent.ParentAttr = attr
	def getAttr(self):
		print "parent attribute :", parent.ParentAttr
class Child(Parent):
	def __init__(self):
		print "calling child constructor"
	def ChildMethod(self):
		print "calling child method"
c = Child()
c.ChildMethod()
c.ParentMethod()
