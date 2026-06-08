username = input("Enter username : ")
password = input("Enter password : ")
age = int(input("Enter your age : "))
plan = input("Enter your plan (Basic / Premium / VIP) : " )

if username == "Anil" and password == "A1234":
    print("Login successful")
else:
    print("wrong credentials, access denied")
    exit()

if age < 13:
    category = "Kids"
elif age < 18:
    category = "Teen"
else:
    category = "Adult"

if plan not in ["Basic", "Premium", "VIP"]:
    print("Invalid plan. Choose Basic, Premium or VIP")

if plan == "Premium" or plan == "VIP":
    hd = "yes"
else:
    hd = "no"

if plan=="Basic":
    screen = 1
    price = 99
elif plan=="Premium":
    screen = 3
    price =299
elif plan=="VIP":
    screen = 5
    price = 599
print("------------------------------------")
print(f"Welcome {username}")
print(f"plan: {plan.upper()} | {price}/month")
print(f"screens: {screen} | HD: {hd}")
print(f"Content category: {category}")