from user import User
from validate import *

if __name__ == "__main__":
    print "hello user enter you login detail"
    username = raw_input("Enter username: ")
    password = raw_input("Enter password: ")
    user = User(username,password)
    validate = Validate()
    validate.adduser(user)
    '''
        create database userexp;
        create table user(
            name varchar(50),
            password varchar(50)
        );
    '''
