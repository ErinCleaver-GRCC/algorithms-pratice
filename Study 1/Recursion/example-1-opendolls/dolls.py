# goes throug the function
def openRussianDoll(doll):
    # when the value reachs 1 it will leave the recursive fuction
    if doll == 1:
        print("Removed doll number ", doll)
        print("All dolls are opened")
    else:
        #otherwise it will run the function recursive and take away one
        print("Removed doll number ", doll)
        openRussianDoll(doll-1)

openRussianDoll(5)       

