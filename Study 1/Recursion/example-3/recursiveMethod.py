def recursiveMethod(n):
    # exits out of the recursive method if it is less then one and prints a message.
    if n<1:
        print("n is less than 1")
        # calls the recursive method if it is more then 1 and subtracts one.
        # to stop users from entering things other then Integer you would need to add a test.
    else: 
        recursiveMethod(n-1)