print("------------------------------------------------------------------------------------------------------------------------------------\n\n")
print("Welcome to our Multiple data operations program!!!\n\n")
print("------------------------------------------------------------------------------------------------------------------------------------\n\n")
print("1-Reverse a stack(dynamic)/ Perform operatiions on given Stack.")
print("2-Calculate the factorial for a given number.")
print("3-Determine the fibo number for the specified term(from 1).")
print("4-Determine the fibo number for the specified term(from 0).")
print("5-Determine the sum upto specified fibo term and display overall details.\n\n")
print("------------------------------------------------------------------------------------------------------------------------------------\n")
Sum_1=0
Count_1=0
Sum_0=0
Count_0=0
def Stack_Reversal():
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to stack Menu")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("Please make your choice-")
    print("1.Append an integer into stack")
    print("2.Enter a decimal number into stack")
    print("3.Enter a string into stack")
    S=[]
    c=''
    while c in 'Yy':
        try:
            T=int(input("Make your choice from Stack menu:-"))
            if T==1:
                R=int(input("Enter the integer:"))
                S.append(R)
                print("Done!")
            elif T==2:
                K=float(input("Enter the decimal number:"))
                S.append(K)
                print("Done!")
            elif T==3:
                N=str(input("Enter the string:"))
                S.append(N)
                print("Done!")
            else:
                print("Please give the input within specified range!!")
        except Exception as e:
            print("Please enter valid datatype(Integer)!!")
        c=input("Want to continue?:(Y/N)-")
    print("\nThe stack is:-",S)
    L=[]
    def Stack(S):
        if S==[]:
            return []
        else:
            L=[S[-1]]+Stack(S[:-1])
            return L
    return f"\nThe reversed stack is:-{Stack(S)}"

def factorial_for_number(): #Error handling to be coded later!
    n=int(input("Enter the term for accessing its factorial:-"))
    print("The factorial is:-",end='')
    def factorial(n):
        if n==1:
            print("1",end='')
            return 1
        else:
            print(f"{n}*",end='')
            return n*factorial(n-1)
    return f"={factorial(n)}"
def fibo_number_1(): #Error handling to be coded later!
    global Sum_1, Count_1, n_1
    n_1=int(input("Enter the term no. for accessing the fibo number/fibo sum at that position- (Starting from 1):-"))
    a=0
    b=1
    c=0
    def fibo_1(n_1):
        global Sum_1, Count_1
        nonlocal a,b,c
        for x in range(0,n_1):
            Count_1+=1
            c+=1
            a,b=b,a+b
            Sum_1+=a
            print(f"Factorial at Iteration-{c}={a}")
        print("Therefore, the overall fibo number (Starting from 1) for the given term is:-",a)
        return f"The no. of terms are:-{c}"
    return fibo_1(n_1)

def fibo_number_0(): #Error handling to be coded later!
    global Sum_0, Count_0, n_0
    n_0=int(input("Enter the term no. for accessing the fibo number/fibo sum at that position- (Starting from 0):-"))
    a=1
    b=0
    c=0
    def fibo_0(n_0):
        nonlocal a,b,c
        global Sum_0, Count_0
        for x in range(0,n_0):
            Count_0+=1
            c+=1
            a,b=b,a+b
            Sum_0+=a
            print(f"Factorial at Iteration-{c}={a}")
        print("Therefore, the overall fibo number (Starting from 0) for the given term is:-",a)
        return f"The no. of terms are:-{c}"
    return fibo_0(n_0)
    
def sum_fibo_series(): #Error handling to be coded later!
    T=print("Want to access the fibo sum and details from (1 or 0)?")
    H=int(input("Specify your choice (1/0):-"))
    if H==1:
        return f"{fibo_number_1()}\nThe sum upto given fibo number ({n_1}) is:-{Sum_1}"
    elif H==0:
        return f"{fibo_number_0()}\nThe sum upto given fibo number ({n_0}) is:-{Sum_0}"
c=''
while c.lower() in 'y':
    try:
        T=int(input("Make your choice from main menu:-"))
        if T==1:
            print(Stack_Reversal())
        elif T==2:
            print(factorial_for_number())
        elif T==3:
            print(fibo_number_1())
        elif T==4:
            print(fibo_number_0())
        elif T==5:
            print(sum_fibo_series())
        else:
            print("Please give the input within the specified range!")
    except Exception as e:
        print("Please enter valid datatype(Integer)!!")
    c=input("\nWant to continue?:(Y/N)-")
    while c not in 'YyNn':
        print("Please enter a valid choice!")
        c=input("Want to continue?:(Y/N)-")
    if c.lower()=='n':
        print("Thanks for visiting our program!!")
        print("Have a good day!!")
        exit()
    
        
        
            
            
    
        
        
    
    
        
          
    
    

