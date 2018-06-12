hello = 'hello'    # String literals can use single quotes
world = "world"    # or double quotes; it does not matter.
print(hello)       # Prints "hello"
print(len(hello))  # String length; prints "5"
hw = hello+' '+world  # String concatenation
print(hw)  # prints "hello world"
hw1= '%s %s %d' % (hello,world,1)  # sprintf style string formatting
print(hw1)  # prints "hello world 12"

