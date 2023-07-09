import random 
print("WELCOME TO THE GAME:- ")
print("First is computer's chance to choose\n   \n Now its your chance to choose") 
print("\n")
user_input=input('''OPTIONS: Choose S for Snake \n Choose W for Water \n Choose G for Gun \n Your option: ''')
print()

comp=random.randrange(1,4)
if comp==1:
    Comp='S'
elif comp==2:
    comp='W'
else:
    comp='G'
print("computer choosed",comp)
def gamewin():
    if user_input==Comp:
        print("It's a Tie !")
    elif user_input=='W':
        if comp=='S':
            return False
        elif comp=='G':
            return True
    elif user_input=='G':
        if comp=='S':
            return True
        elif comp=='G':
            return False
    elif user_input=='S':
        if comp=='W':
            return True
        elif comp=='G':
            return False

if True:
    print("You WON !")
else:
    print("You Lost !")
