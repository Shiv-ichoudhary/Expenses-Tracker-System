# Expense Tracker Project

expenses = [] # list of all expenses in form of dictionary
print("Welcome to Expense Tracker : Save Money ")

while True:
    print("======MENU======")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Kharch")
    print("4. Exit")

    choice = int(input("please enter your choice"))

    if(choice==1):
        date = input("Which expense happened on which date?")
        category = input("What type of expense did you make?")
        Discription = input("add details")
        amount = float(input("enter the amount:  "))

        expense ={
            "date": date,
            "category": category,
            "description": Discription,
            "amount": amount
        }

        expenses.append(expense)
        print("\n Done  Expens is added sucessfully")


#2. View all expenses

    elif(choice == 2):
        if( len(expenses)==0):
             print("no expenses added. jao phele kharcha karo")
        else:
            print("===ye h apka sara expenses====")
            count= 1
            for eachkharcha in expenses:
               print(f"kharcha Number {count} -> {eachkharcha['date']}, {eachkharcha['category']}, {eachkharcha['description']}, {eachkharcha['amount']}")
               count =count+1

# view total spending

    elif(choice ==3):                
            total =0
            for eachkharcha in expenses:
                total =total + eachkharcha["amount"]

            print("\n Total kharcha =", total)   

#4 Exit
    elif(choice ==4):
         print("Thank you for using our system")
         break
    else:
         print("invalid choice")