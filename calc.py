def cal():
    i = (input(''''  Enter a or A to Addition
                  Enter s or S to subtraction
                  Enter m or M to Multiply
                  Enter d or D to Divide ->'''))
    if   i == "a" or i =="A":
        r = float(input("Enter First number: "))
        f = float(input("Enter second number: "))
        print(r+f)
    elif i == "s" or i == "S":
        t = float(input("Enter first Number: "))
        m = float(input("Enter second Number: "))
        print(t-m)
    elif i == "d" or i == "D":
        t = float(input("Enter first Number: "))
        m = float(input("Enter second Number: "))
        print(t/m)
    elif i == "m" or i == "M":
        t = float(input("Enter first Number: "))
        m = float(input("Enter second Number: "))
        print(t*m)
    
while True:
    cal()
    w = input("Enter Q or q for quit or C or c to continue: ")
    if w == "Q" or w == "q":
        break
    elif w == "c" or w == "C":
        pass