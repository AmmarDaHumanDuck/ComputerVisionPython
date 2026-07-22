print ("Welcome to the Python Calculator")
print ("Please start by inputting a number from 1 to 4 for the following options: \n Choose operation:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")

choice = input("Choice: ")

if choice == "1":
    print ("You have chosen addition, please input two numbers to add")
    add_1 = float(input("First number: "))
    add_2 = float(input("Second number: "))
    add = add_1 + add_2 
    print("The answer is: " + str(add))

elif choice == "2":
    print ("You have chosen subtraction, please input two numbers to subtract")
    sub_1 = float(input("First number: "))
    sub_2 = float(input("Second number: "))
    sub = sub_1 - sub_2 
    print("The answer is: " + str(sub))

elif choice == "3":
    print ("You have chosen multiplication, please input two numbers to multiply")
    mult_1 = float(input("First number: "))
    mult_2 = float(input("Second number: "))
    mult = mult_1 * mult_2 
    print("The answer is: " + str(mult))

elif choice == "4":
    print ("You have chosen division, please input two numbers to divide")
    div_1 = float(input("First number: "))
    div_2 = float(input("Second number: "))
    div = div_1 / div_2 
    print("The answer is: " + str(div))
else: 
    print("bye bye")