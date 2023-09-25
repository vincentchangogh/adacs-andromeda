#!usr/bin/env python3

# If you run the function from this module after importing the module in Python, it
# will print You just ran the function called func from module mymodule
def func():
    print("You just ran the function called `func` from module `mymodule'")


# If you are running the file from the terminal, it will print Hello from module
# mymodule

if __name__ == "__main__":
    print("Hello from module 'mymodule'")
# If you are importing the module from Python, it will print 'You imported the module'
else:
    print("You imported the module")
