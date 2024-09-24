def task_1():
    password = "Password123"

    guess = ""
    
    while guess != password:
     guess = input ("please enter the password: ");
       

def task_2(): # Times table

    # Enter your code here
    table = int(input("Select time table:" ))

    terms = int(input("how many terms to calculate:"))

    counter = 1
    
    while  counter <= terms:
       print(table*counter)
       counter += 1; 

def task_3(): # Count mississippis
    
    import time
     counter = 0
     while counter <5:
        print(f"{counter + 1} mississipi")
        time.sleep(1)
        print(task_3)
