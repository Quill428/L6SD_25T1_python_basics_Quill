""""
#Si 1 and Si 5 simple calculator 
print('Enter a number')
x = int(input())
print('Enter another number')
y = int(input())
print('Enter a number dpending on what you want')
print('1 = add, 2 = minus, 3 = times, 4 = Divide')
z = int(input())


if z == 1:
    a = x + y
    print (a)

4
elif z == 2:
    b = x - y
    print (b)

elif z == 3:
    c = x * y
    print (c) 

elif z == 4:
    d = x / y
    print (d)

else:
    print("try again")


#even or odd
print("enter a number")
num = int(input())

if num % 2 == 0:
    print("that number is even")
else:
    print("that number is odd")


#SI 3 getting the right age
print ("enter age")
age = int(input())
if age >= 18:
    print("you are old enough to vote")

else:
    print("you are NOT old enough")

#Si 4 calculating 

a = 5 * 2 + 3 
print(a)
'''
5 * 2 + 3 the code is lined up to solve the soultion
* is multiplying the 5 and the 2 getting a result of 10
after its adding together the 10 and the 3 getting the result of 13
the "a" at the start is taking the result of the result which is 13 
and the print(a) is printing the result which gives us the 13 
'''
"""
#Day 2 
print("What is your name?")
name = input()
print("and how old are you?") 
age = int(input())
print("good evening " + name + " or pherhaps good afternoon. i want to add something can you enter your first number to add")
num1 = int(input())
print(str(num1) + " and what other number")
num2 = int(input())
num3 = num1 + num2
print("the sum of " + str(num1) + " and " + str(num2) + " adds up to the total of " + str(num3))
print("that was fun how about i get to learn you what is your favourite colour")
Colour = input()
print(Colour + " is a really good colour but i like " + Colour + " more")
print("wait its the same colour")

print("what would you like to see next")
print("1 = Outputs, 2 = Variables, or 3 = Control Flow ")
result = int(input())

if result == 1:
    
    print("so you are " + name + "\nand you are " + str(age) + " years old") #\n breaks the line and add the rest of the line into the next line
    i = 1
    while i < 6: #Loop
        print("Hello " + name)
        i += 1

elif result == 2:
    print("quick math problem\nwhat does 1+1=?")
    in1 = int(input())
    print("and what does 2+2=?")
    in2 = int(input())
    in1, in2 = in2, in1
    print("...\num idon't know how to tell you this but 1+1 doesn't equal " + str(in1))
    print("and 2+2 doesn't equal " + str(in2))
    print("oops there was a problem can you reenter your age")
    age2 = int(input())
    if age == age2:
        if age == 21:
            print("i just wanted to make sure glad to hear you are " + str(age) + " i am 21 as well")

        elif age > 21:
            print("i just wanted to make sure glad to hear you are " + str(age) + " i am 21 which is younger")

        else:
            print("i just wanted to make sure glad to hear you are " + str(age) + " i am 21 which is older")
    elif age2 == age + 1:
        print("did you have your birthday just now?")

    elif age > age2:
        print("did you get younger suddendly?")

    else:
        print("did you get older suddendly?")
    """
        #this code is shown a lot online but the line above is the simpler verison
        x = 10
        y = 50
        
        temp = x
        x = y #this line is replacing the valuse of Y with X 
        y = temp
        
        print("Value of x:", x)
        print("Value of y:", y)
    """
else:
    b = 1
    while b < 10: #Loop
        print(b)
        b += 1
    print("pick a number between 1 and 3")
    