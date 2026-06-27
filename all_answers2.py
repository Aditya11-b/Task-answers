
 Q1 - Student Attendance

Count total present students from attendance list

def count_attendance(attendance):
    present = attendance.count('P')
    print(f"Total Present: {present}")
    print(f"Total Absent: {len(attendance) - present}")

count_attendance(['P', 'A', 'P', 'P', 'A'])

 Output
 Total Present: 3
 Total Absent: 2


 Q2 - Login System
 Check if entered password matches 'admin123'

def login(password):
    if password == 'admin123':
        print("Access Granted")
    else:
        print("Access Denied")

login("admin123")   # Access Granted
login("wrongpass")  # Access Denied

 Output:
 Access Granted
 Access Denied



 Q3 - Electricity Bill

 Calculate bill: 0-100 = ₹1/unit, 101-200 = ₹2/unit, >200 = ₹3/unit

def electricity_bill(units):
    if units <= 100:
        bill = units * 1
    elif units <= 200:
        bill = 100 * 1 + (units - 100) * 2
    else:
        bill = 100 * 1 + 100 * 2 + (units - 200) * 3
    print(f"Units consumed: {units}")
    print(f"Total Bill: ₹{bill}")

electricity_bill(250)

 Output:
 Units consumed: 250
 Total Bill: ₹450


 
 Q4 - Name Formatter

 Capitalize first letter of each word

def format_name(name):
    formatted = name.title()
    print(f"Formatted Name: {formatted}")

format_name("rahul kumar sharma")

 Output:
 Formatted Name: Rahul Kumar Sharma



 Q5 - Mobile Recharge
 
 Return validity days for ₹199 or ₹399, else invalid

def mobile_recharge(amount):
    plans = {
        199: 28,
        399: 84
    }
    if amount in plans:
        print(f"Recharge of ₹{amount} successful! Validity: {plans[amount]} days")
    else:
        print("Invalid recharge amount")

mobile_recharge(199)
mobile_recharge(399)
mobile_recharge(500)

 Output:
 Recharge of ₹199 successful! Validity: 28 days
 Recharge of ₹399 successful! Validity: 84 days
 Invalid recharge amount



 Q6 - E-commerce Cart
 
 Calculate total bill from list of items with price and quantity

def calculate_cart(cart):
    total = 0
    print("--- Cart Summary ---")
    for item in cart:
        subtotal = item['price'] * item['quantity']
        print(f"{item['name']}: ₹{item['price']} x {item['quantity']} = ₹{subtotal}")
        total += subtotal
    print(f"Total Bill: ₹{total}")

cart = [
    {'name': 'Shirt',  'price': 500,  'quantity': 2},
    {'name': 'Jeans',  'price': 1200, 'quantity': 1},
    {'name': 'Shoes',  'price': 800,  'quantity': 1},
]
calculate_cart(cart)

 Output:
  Cart Summary 
 Shirt: ₹500 x 2 = ₹1000
 Jeans: ₹1200 x 1 = ₹1200
 Shoes: ₹800 x 1 = ₹800
 Total Bill: ₹3000



 Q7 - Salary Calculator
 
 Final Salary = Basic + HRA (20%) + DA (10%)

def calculate_salary(basic):
    hra = basic * 0.20
    da  = basic * 0.10
    final = basic + hra + da
    print(f"Basic Salary : ₹{basic}")
    print(f"HRA (20%)    : ₹{hra}")
    print(f"DA  (10%)    : ₹{da}")
    print(f"Final Salary : ₹{final}")

calculate_salary(30000)

 Output:
 Basic Salary : ₹30000
 HRA (20%)    : ₹6000.0
 DA  (10%)    : ₹3000.0
 Final Salary : ₹39000.0


 
 Q8 - OTP Verification
 
 Generate OTP and allow 3 attempts to verify

import random

def otp_verification():
    otp = random.randint(100000, 999999)
    print(f"Your OTP is: {otp}")  # In real apps, sent via SMS/email

    for attempt in range(1, 4):
        entered = int(input(f"Attempt {attempt}/3 - Enter OTP: "))
        if entered == otp:
            print("OTP Verified! Access granted.")
            return
        else:
            print("Incorrect OTP.")

    print("Too many failed attempts. Access blocked.")

 Sample Output (when correct OTP entered on attempt 1):
 Your OTP is: 483921
 Attempt 1/3 - Enter OTP: 483921
 OTP Verified! Access granted.

 Sample Output (all 3 attempts wrong):
 Your OTP is: 738104
 Attempt 1/3 - Enter OTP: 000000
 Incorrect OTP.
 Attempt 2/3 - Enter OTP: 111111
 Incorrect OTP.
 Attempt 3/3 - Enter OTP: 222222
 Incorrect OTP.
 Too many failed attempts. Access blocked.

 otp_verification()  Uncomment to run interactively

 
 Q9 - Banking System

 Deposit, withdraw, and check balance
def banking_system():
    balance = 0

    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == '1':
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited. New Balance: ₹{balance}")
            else:
                print("Invalid amount.")

        elif choice == '2':
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount > balance:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn. Remaining Balance: ₹{balance}")

        elif choice == '3':
            print(f"Current Balance: ₹{balance}")

        elif choice == '4':
            print("Thank you for banking with us!")
            break

        else:
            print("Invalid option. Try again.")

 Sample Output:
 --- Banking Menu ---
 1. Deposit  2. Withdraw  3. Check Balance  4. Exit
 Choose option: 1
 Enter deposit amount: ₹5000
 ₹5000.0 deposited. New Balance: ₹5000.0
 Choose option: 2
 Enter withdrawal amount: ₹2000
 ₹2000.0 withdrawn. Remaining Balance: ₹3000.0
 Choose option: 3
 Current Balance: ₹3000.0
 Choose option: 4
 Thank you for banking with us!

banking_system()  # Uncomment to run interactively


 Q10 - Food Ordering System
 
 Menu with multiple orders + 5% GST on total

def food_ordering():
    menu = {
        1: ('Burger',    120),
        2: ('Pizza',     250),
        3: ('Pasta',     180),
        4: ('Sandwich',   90),
        5: ('Cold Drink', 50),
    }

    print("--- Welcome to Food Corner ---")
    print("\nMenu:")
    for key, (name, price) in menu.items():
        print(f"  {key}. {name} - ₹{price}")

    order_total = 0
    orders = []

    while True:
        choice = input("\nEnter item number to order (or 0 to checkout): ")
        if choice == '0':
            break
        if not choice.isdigit() or int(choice) not in menu:
            print("Invalid choice. Try again.")
            continue

        item_no = int(choice)
        qty = int(input(f"Enter quantity for {menu[item_no][0]}: "))
        subtotal = menu[item_no][1] * qty
        orders.append((menu[item_no][0], menu[item_no][1], qty, subtotal))
        order_total += subtotal
        print(f"Added {qty}x {menu[item_no][0]} = ₹{subtotal}")

    gst = order_total * 0.05
    grand_total = order_total + gst

    print("\n--- Order Summary ---")
    for name, price, qty, subtotal in orders:
        print(f"  {name} x{qty} @ ₹{price} = ₹{subtotal}")
    print(f"Subtotal : ₹{order_total:.2f}")
    print(f"GST (5%) : ₹{gst:.2f}")
    print(f"Total    : ₹{grand_total:.2f}")
    print("Thank you for your order!")

 Sample Output:
 --- Welcome to Food Corner ---
 Menu:
   1. Burger - ₹120
   2. Pizza - ₹250
   3. Pasta - ₹180
   4. Sandwich - ₹90
   5. Cold Drink - ₹50
 Enter item number (or 0 to checkout): 1
 Enter quantity for Burger: 2
 Added 2x Burger = ₹240
 Enter item number (or 0 to checkout): 5
 Enter quantity for Cold Drink: 2
 Added 2x Cold Drink = ₹100
 Enter item number (or 0 to checkout): 0
 --- Order Summary ---
   Burger x2 @ ₹120 = ₹240
   Cold Drink x2 @ ₹50 = ₹100
 Subtotal : ₹340.00
 GST (5%) : ₹17.00
 Total    : ₹357.00
 Thank you for your order!

 food_ordering()  # Uncomment to run interactively
