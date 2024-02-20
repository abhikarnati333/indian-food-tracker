import json

time=input("What do you want to log? \n 1. Breakfast \n 2. Lunch \n 3. Snack \n 4. Dinner \n") 

print("--------------------")

with open('foods.json', 'r') as file:
    data = json.load(file)
    food = data['food']
    
s=0 #Calorie Counter
efood=input("Press Enter two times to exit \n Enter a food name = ")

while efood: 
    new_var = (food[efood])
    print ("Calories for 1 serving of",efood, "is",new_var)
    s=s+new_var
    efood=input("Enter a food name = ")
      
print("--------------------")
print ("Total Calories for",time, "is",s)
print("--------------------")

with open('macfoods.json', 'r') as file:
    data = json.load(file)
    macfood = data['macfood']

macefood=input("Detailed Macro View Per Serving \n Enter a food name = ") #Macros Counter

while macefood:
    print("--------------------")
    print("Calories per serving in",macefood, "is" ,macfood[macefood][0],"g")
    print("Carbs per serving in",macefood, "is" ,macfood[macefood][1],"g")
    print("Protein per serving in",macefood, "is" ,macfood[macefood][2],"g")
    print("Fat per serving in",macefood, "is" ,macfood[macefood][3],"g")
    print("--------------------")
    macefood=input("Enter a food name = ")
    
print("--------------------")

choice=input("Want to use a calculator to calculate the macros? \n 1. Yes \n 2. No \n ") #Calculator

if choice == "Yes" or "yes":
    num1=float(input("Enter a number = "))
    num2=float(input("Enter another number = "))
    opchoice=int(input("Choose an option \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n"))
    print("--------------------")
    if opchoice == 1:
        sum=num1+num2
        print("The sum is",sum)
    elif opchoice == 2:
        if num1<num2:
            diff=num2-num1
            print("The difference is",diff)
        else:
            diff=num1-num2
            print("The difference is",diff)
    elif opchoice == 3:
        pro=num1*num2
        print("The product is",pro)
    elif opchoice == 4:
        if num1<num2:
            rem=num2/num1
            print("The answer is",rem)
        else:
            rem=num1/num2
            print("The answer is",rem)
    else:
        print("Error")
        
elif choice == "No" or "no":
    print("Thank you for using this program")



